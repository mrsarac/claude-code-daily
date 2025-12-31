#!/usr/bin/env python3
"""
Claude Code Daily - Automated Tip Curator

This script runs daily to:
1. Scrape Twitter for #ClaudeCode hashtag
2. Scrape Reddit r/ClaudeAI for tips
3. Use Gemini AI to validate and categorize
4. Deduplicate against existing tips
5. Update repository files
"""

import os
import json
import hashlib
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Configuration
CONFIG = {
    "twitter": {
        "hashtags": ["ClaudeCode", "ClaudeDev"],
        "accounts": ["anthropic", "alexalbert__", "AmandaAskell"],
        "min_likes": 5,
        "max_age_days": 7
    },
    "reddit": {
        "subreddits": ["ClaudeAI", "claudeai"],
        "min_score": 10,
        "max_age_days": 7
    },
    "categories": [
        "orchestration",
        "context-management",
        "workflow",
        "subagents",
        "tooling"
    ]
}


def get_existing_tips():
    """Load existing tips to check for duplicates."""
    tips_dir = Path("tips")
    all_tips = {"tips": [], "hashes": set()}

    # Scan all category directories
    for category in CONFIG["categories"]:
        category_dir = tips_dir / category
        if category_dir.exists():
            for tip_file in category_dir.glob("*.md"):
                content = tip_file.read_text()
                # Extract title from first line
                lines = content.strip().split('\n')
                if lines:
                    title = lines[0].replace('#', '').strip()
                    all_tips["tips"].append({"title": title, "file": str(tip_file)})
                    all_tips["hashes"].add(generate_tip_hash(title))

    return all_tips


def generate_tip_hash(tip_text: str) -> str:
    """Generate a hash for deduplication."""
    normalized = tip_text.lower().strip()
    # Remove common words for better matching
    for word in ["the", "a", "an", "to", "for", "in", "on", "with"]:
        normalized = normalized.replace(f" {word} ", " ")
    return hashlib.md5(normalized.encode()).hexdigest()[:12]


def fetch_twitter_tips():
    """
    Fetch tips from Twitter/X using API v2.

    Requires TWITTER_BEARER_TOKEN environment variable.
    """
    token = os.getenv("TWITTER_BEARER_TOKEN")
    if not token:
        print("⚠️  Twitter: No bearer token found, skipping...")
        return []

    tips = []
    headers = {"Authorization": f"Bearer {token}"}

    # Search for Claude Code related tweets
    for hashtag in CONFIG["twitter"]["hashtags"]:
        query = f"#{hashtag} -is:retweet lang:en"
        url = "https://api.twitter.com/2/tweets/search/recent"
        params = {
            "query": query,
            "max_results": 50,
            "tweet.fields": "created_at,public_metrics,author_id",
            "expansions": "author_id",
            "user.fields": "username"
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)

            if response.status_code == 200:
                data = response.json()
                tweets = data.get("data", [])
                users = {u["id"]: u["username"] for u in data.get("includes", {}).get("users", [])}

                for tweet in tweets:
                    metrics = tweet.get("public_metrics", {})
                    likes = metrics.get("like_count", 0)

                    # Filter by minimum likes
                    if likes >= CONFIG["twitter"]["min_likes"]:
                        tips.append({
                            "title": tweet["text"][:100],
                            "content": tweet["text"],
                            "source": "twitter",
                            "author": users.get(tweet.get("author_id"), "unknown"),
                            "url": f"https://twitter.com/i/status/{tweet['id']}",
                            "likes": likes,
                            "created_at": tweet.get("created_at")
                        })

                print(f"🐦 Twitter #{hashtag}: Found {len(tweets)} tweets, {len([t for t in tips if hashtag.lower() in t.get('content', '').lower()])} quality tips")

            elif response.status_code == 429:
                print(f"⚠️  Twitter: Rate limited, skipping #{hashtag}...")
            else:
                print(f"⚠️  Twitter #{hashtag}: API error {response.status_code}")

        except Exception as e:
            print(f"⚠️  Twitter #{hashtag}: Error - {str(e)[:50]}")

    print(f"🐦 Twitter: Total {len(tips)} quality tips found")
    return tips


def fetch_reddit_tips():
    """
    Fetch tips from Reddit using PRAW.

    Requires REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET.
    """
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("⚠️  Reddit: No credentials found, skipping...")
        return []

    tips = []

    try:
        import praw

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent="claude-code-daily/1.0"
        )

        for subreddit_name in CONFIG["reddit"]["subreddits"]:
            try:
                subreddit = reddit.subreddit(subreddit_name)

                # Get hot and new posts from last week
                for post in subreddit.hot(limit=50):
                    # Check age
                    post_age = datetime.utcnow() - datetime.utcfromtimestamp(post.created_utc)
                    if post_age.days > CONFIG["reddit"]["max_age_days"]:
                        continue

                    # Check score
                    if post.score >= CONFIG["reddit"]["min_score"]:
                        # Look for tip-like content
                        content = f"{post.title}\n\n{post.selftext}" if post.selftext else post.title

                        if any(kw in content.lower() for kw in ["tip", "trick", "workflow", "claude code", "context", "subagent"]):
                            tips.append({
                                "title": post.title[:100],
                                "content": content,
                                "source": "reddit",
                                "author": str(post.author),
                                "url": f"https://reddit.com{post.permalink}",
                                "score": post.score,
                                "created_at": datetime.utcfromtimestamp(post.created_utc).isoformat()
                            })

                print(f"🤖 Reddit r/{subreddit_name}: Found tips")

            except Exception as e:
                print(f"⚠️  Reddit r/{subreddit_name}: Error - {str(e)[:50]}")

    except ImportError:
        print("⚠️  Reddit: PRAW not installed, using API directly...")
        # Fallback to direct API (read-only, no auth needed for public posts)
        for subreddit_name in CONFIG["reddit"]["subreddits"]:
            try:
                url = f"https://www.reddit.com/r/{subreddit_name}/hot.json?limit=50"
                headers = {"User-Agent": "claude-code-daily/1.0"}
                response = requests.get(url, headers=headers, timeout=30)

                if response.status_code == 200:
                    data = response.json()
                    posts = data.get("data", {}).get("children", [])

                    for post_data in posts:
                        post = post_data.get("data", {})
                        score = post.get("score", 0)

                        if score >= CONFIG["reddit"]["min_score"]:
                            content = f"{post.get('title', '')}\n\n{post.get('selftext', '')}"

                            if any(kw in content.lower() for kw in ["tip", "trick", "workflow", "claude", "context"]):
                                tips.append({
                                    "title": post.get("title", "")[:100],
                                    "content": content,
                                    "source": "reddit",
                                    "author": post.get("author", "unknown"),
                                    "url": f"https://reddit.com{post.get('permalink', '')}",
                                    "score": score
                                })

                    print(f"🤖 Reddit r/{subreddit_name}: Found {len([t for t in tips if subreddit_name.lower() in t.get('url', '').lower()])} tips")

            except Exception as e:
                print(f"⚠️  Reddit r/{subreddit_name}: Error - {str(e)[:50]}")

    print(f"🤖 Reddit: Total {len(tips)} tips found")
    return tips


def validate_and_categorize(tips: list) -> list:
    """
    Use Gemini AI to validate tips and assign categories.

    Requires GEMINI_API_KEY environment variable.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or not tips:
        if not api_key:
            print("⚠️  Gemini: No API key found, skipping validation...")
        return tips

    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        validated_tips = []

        for tip in tips:
            prompt = f"""Analyze this potential Claude Code tip and respond with JSON only:

Content: {tip.get('content', '')[:500]}

Tasks:
1. Is this a useful Claude Code tip? (true/false)
2. Rate quality 1-10
3. Assign category: orchestration, context-management, workflow, subagents, or tooling
4. Write a concise title (max 60 chars)
5. Write a one-paragraph summary

Respond ONLY with valid JSON:
{{"is_valid": true/false, "quality": 1-10, "category": "string", "title": "string", "summary": "string"}}"""

            try:
                response = model.generate_content(prompt)
                result_text = response.text.strip()

                # Clean up response
                if result_text.startswith("```"):
                    result_text = result_text.split("```")[1]
                    if result_text.startswith("json"):
                        result_text = result_text[4:]

                result = json.loads(result_text)

                if result.get("is_valid") and result.get("quality", 0) >= 6:
                    tip["category"] = result.get("category", "workflow")
                    tip["ai_title"] = result.get("title", tip["title"])
                    tip["summary"] = result.get("summary", "")
                    tip["quality"] = result.get("quality", 5)
                    validated_tips.append(tip)

            except Exception as e:
                print(f"⚠️  Gemini validation error: {str(e)[:30]}")
                # Keep tip without AI validation
                tip["category"] = "workflow"
                validated_tips.append(tip)

        print(f"✨ Gemini: Validated {len(validated_tips)}/{len(tips)} tips")
        return validated_tips

    except ImportError:
        print("⚠️  Gemini: google-generativeai not installed")
        return tips


def deduplicate(new_tips: list, existing_tips: dict) -> list:
    """Remove tips that already exist in the repository."""
    existing_hashes = existing_tips.get("hashes", set())

    unique_tips = []
    for tip in new_tips:
        # Check title hash
        title_hash = generate_tip_hash(tip.get("ai_title", tip.get("title", "")))
        content_hash = generate_tip_hash(tip.get("content", "")[:200])

        if title_hash not in existing_hashes and content_hash not in existing_hashes:
            unique_tips.append(tip)
            existing_hashes.add(title_hash)

    return unique_tips


def create_tip_file(tip: dict, tip_number: int) -> Optional[Path]:
    """Create a markdown file for a new tip."""
    category = tip.get("category", "workflow")
    category_dir = Path(f"tips/{category}")
    category_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    title_slug = tip.get("ai_title", tip.get("title", "tip"))[:40]
    title_slug = "".join(c if c.isalnum() or c == " " else "" for c in title_slug)
    title_slug = title_slug.strip().replace(" ", "-").lower()

    filename = f"{tip_number:03d}-{title_slug}.md"
    filepath = category_dir / filename

    # Create content
    content = f"""# {tip.get('ai_title', tip.get('title', 'Tip'))}

{tip.get('summary', tip.get('content', '')[:300])}

## Source

- **Author:** {tip.get('author', 'Community')}
- **Platform:** {tip.get('source', 'unknown').title()}
- **Link:** [{tip.get('source', 'source')}]({tip.get('url', '#')})
- **Added:** {datetime.now().strftime('%Y-%m-%d')}

## Tags

`#{category}` `#claude-code` `#tip`
"""

    filepath.write_text(content)
    return filepath


def update_index(new_tips: list):
    """Update the tips/index.json file."""
    index_file = Path("tips/index.json")

    if index_file.exists():
        with open(index_file) as f:
            index = json.load(f)
    else:
        index = {"categories": [], "totalTips": 0, "lastUpdated": ""}

    # Update counts
    for tip in new_tips:
        category = tip.get("category", "workflow")
        # Find or create category in index
        cat_entry = next((c for c in index["categories"] if c["name"] == category), None)
        if not cat_entry:
            cat_entry = {"name": category, "count": 0}
            index["categories"].append(cat_entry)
        cat_entry["count"] = cat_entry.get("count", 0) + 1

    index["totalTips"] = index.get("totalTips", 0) + len(new_tips)
    index["lastUpdated"] = datetime.now().isoformat()

    with open(index_file, "w") as f:
        json.dump(index, f, indent=2)


def update_readme_today_tip(new_tips: list):
    """Update the 'Today's Tip' section in README."""
    readme_path = Path("README.md")
    if not readme_path.exists():
        return

    content = readme_path.read_text()

    # If we have new tips, feature one
    if new_tips:
        tip = new_tips[0]
        today_tip = f"""## 💡 Today's Tip

> **{tip.get('ai_title', tip.get('title', 'New Tip'))}**
>
> {tip.get('summary', tip.get('content', ''))[:200]}...
>
> — *{tip.get('author', 'Community')}* via {tip.get('source', 'community').title()}

"""
        # Replace existing Today's Tip section
        import re
        pattern = r"## 💡 Today's Tip.*?(?=##|\Z)"
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, today_tip, content, flags=re.DOTALL)

        readme_path.write_text(content)
        print(f"📝 README: Updated Today's Tip")
    else:
        print("📝 README: No new tips to feature")


def update_repository(tips: list):
    """Add new tips to the appropriate category files."""
    if not tips:
        print("✅ No new tips to add today.")
        return

    print(f"📦 Adding {len(tips)} new tips...")

    # Get current tip count for numbering
    existing = get_existing_tips()
    tip_number = len(existing.get("tips", [])) + 1

    created_files = []
    for tip in tips:
        filepath = create_tip_file(tip, tip_number)
        if filepath:
            created_files.append(filepath)
            tip_number += 1

    # Update index
    update_index(tips)

    # Update README
    update_readme_today_tip(tips)

    print(f"✅ Created {len(created_files)} new tip files")


def main():
    print("="*50)
    print(f"🚀 Claude Code Daily - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*50)

    # Load existing tips
    existing = get_existing_tips()
    print(f"📊 Existing tips: {len(existing.get('tips', []))}")

    # Fetch from sources
    twitter_tips = fetch_twitter_tips()
    reddit_tips = fetch_reddit_tips()

    all_new_tips = twitter_tips + reddit_tips
    print(f"🌐 Found {len(all_new_tips)} potential tips")

    if all_new_tips:
        # Validate and categorize
        validated = validate_and_categorize(all_new_tips)

        # Deduplicate
        unique = deduplicate(validated, existing)
        print(f"✨ Unique new tips: {len(unique)}")

        # Update repository
        update_repository(unique)
    else:
        print("📭 No new tips found from sources")

    print("="*50)
    print("✅ Daily update complete!")
    print("="*50)


if __name__ == "__main__":
    main()
