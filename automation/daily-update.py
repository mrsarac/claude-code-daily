#!/usr/bin/env python3
"""
Claude Code Daily - Automated Tip Curator

This script runs daily to:
1. Scrape Twitter for #ClaudeCode hashtag (requires paid API)
2. Scrape Reddit r/ClaudeAI for tips via RSS
3. Use Gemini AI to validate and categorize
4. Deduplicate against existing tips
5. Update repository files

Repository Structure:
  tips/
  ├── categories/
  │   ├── orchestration.md      # Multiple tips in ## N. Title format
  │   ├── context-management.md
  │   ├── workflow.md
  │   ├── subagents.md
  │   └── tooling.md
  └── index.json
"""

import os
import json
import hashlib
import requests
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, List, Dict

# Configuration
CONFIG = {
    "twitter": {
        "hashtags": ["ClaudeCode", "ClaudeDev"],
        "accounts": ["anthropic", "alexalbert__", "AmandaAskell"],
        "min_likes": 5,
        "max_age_days": 7
    },
    "reddit": {
        "subreddits": ["ClaudeAI"],
        "min_score": 10,
        "max_age_days": 7
    },
    "categories": [
        "orchestration",
        "context-management",
        "workflow",
        "subagents",
        "tooling"
    ],
    "category_keywords": {
        "orchestration": ["worktree", "parallel", "agent", "delegate", "orchestrat"],
        "context-management": ["context", "memory", "session", "bridge", "compact"],
        "workflow": ["workflow", "prompt", "plan", "review", "command"],
        "subagents": ["subagent", "spawn", "task", "coordinator", "mcp"],
        "tooling": ["tool", "plugin", "hook", "script", "automation"]
    }
}


def get_existing_tips():
    """Load existing tips to check for duplicates.

    Tips are stored in tips/categories/{category}.md files with format:
    ## N. Tip Title
    **Source:** Author Name
    Content...
    ---
    """
    tips_dir = Path("tips/categories")
    all_tips = {"tips": [], "hashes": set(), "next_number": 51}  # Start after 50 existing

    if not tips_dir.exists():
        print(f"⚠️  Tips directory not found: {tips_dir}")
        return all_tips

    # Scan all category files
    for category in CONFIG["categories"]:
        category_file = tips_dir / f"{category}.md"
        if category_file.exists():
            content = category_file.read_text()
            # Find all tip titles using regex: ## N. Title
            tip_pattern = r'^## (\d+)\. (.+)$'
            for match in re.finditer(tip_pattern, content, re.MULTILINE):
                tip_num = int(match.group(1))
                title = match.group(2).strip()
                all_tips["tips"].append({
                    "number": tip_num,
                    "title": title,
                    "category": category,
                    "file": str(category_file)
                })
                all_tips["hashes"].add(generate_tip_hash(title))
                # Track highest tip number
                if tip_num >= all_tips["next_number"]:
                    all_tips["next_number"] = tip_num + 1

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
            elif response.status_code == 403:
                print(f"⚠️  Twitter #{hashtag}: Access denied (Free tier doesn't include search API)")
                break  # No point trying other hashtags
            else:
                print(f"⚠️  Twitter #{hashtag}: API error {response.status_code}")

        except Exception as e:
            print(f"⚠️  Twitter #{hashtag}: Error - {str(e)[:50]}")

    print(f"🐦 Twitter: Total {len(tips)} quality tips found")
    return tips


def fetch_reddit_tips():
    """
    Fetch tips from Reddit using RSS feed (more reliable than JSON API).

    RSS feeds don't require authentication and are less likely to be blocked.
    """
    tips = []

    print("🤖 Reddit: Using RSS feed (no auth required)...")

    for subreddit_name in CONFIG["reddit"]["subreddits"]:
        try:
            # RSS feed is more reliable than JSON API
            url = f"https://www.reddit.com/r/{subreddit_name}/hot/.rss?limit=50"
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; claude-code-daily/1.0; +https://github.com/mrsarac/claude-code-daily)",
                "Accept": "application/rss+xml, application/xml, text/xml"
            }
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code == 200:
                # Parse RSS/Atom feed
                try:
                    root = ET.fromstring(response.content)
                    # Handle Atom namespace
                    ns = {"atom": "http://www.w3.org/2005/Atom"}

                    entries = root.findall(".//atom:entry", ns)
                    subreddit_tips = 0

                    for entry in entries:
                        title_elem = entry.find("atom:title", ns)
                        content_elem = entry.find("atom:content", ns)
                        link_elem = entry.find("atom:link", ns)
                        author_elem = entry.find("atom:author/atom:name", ns)

                        if title_elem is not None:
                            title = title_elem.text or ""
                            content = content_elem.text if content_elem is not None else title
                            link = link_elem.get("href", "") if link_elem is not None else ""
                            author = author_elem.text if author_elem is not None else "unknown"

                            # Clean HTML from content
                            content = re.sub(r'<[^>]+>', '', content)

                            # Look for Claude Code related content
                            keywords = ["tip", "trick", "workflow", "worktree", "context", "mcp", "subagent", "prompt", "claude code", "hack", "technique", "pattern"]
                            # Negative keywords - filter out non-tips
                            negative_keywords = [
                                # Complaints and rants
                                "appreciation", "rant", "frustrated", "angry", "disappointed",
                                "broken", "bug report", "anyone else", "does anyone",
                                "i believed", "data is gone", "lost my", "help me",
                                # Questions (not tips)
                                "question about", "how do i", "what is", "why does",
                                "can someone", "is there a way", "looking for",
                                # Off-topic
                                "announcement", "hiring", "job", "newsletter",
                                "guitar", "music", "game", "trading", "crypto",
                                "chatgpt", "openai", "gemini", "llama", "mistral",
                                # App showcases (not Claude Code tips)
                                "built an app", "made an app", "created an app",
                                "my app", "check out my", "just launched",
                                # Seeking help
                                "need help", "please help", "struggling with",
                                "not working", "doesn't work", "stopped working"
                            ]
                            content_lower = content.lower()
                            title_lower = title.lower()

                            # Must have positive keywords AND no negative keywords
                            has_positive = any(kw in content_lower for kw in keywords)
                            has_negative = any(nk in title_lower or nk in content_lower[:200] for nk in negative_keywords)

                            if has_positive and not has_negative:
                                tips.append({
                                    "title": title[:100],
                                    "content": content[:500],
                                    "source": "reddit",
                                    "author": author.replace("/u/", ""),
                                    "url": link,
                                    "score": 0  # RSS doesn't include score
                                })
                                subreddit_tips += 1

                    print(f"🤖 Reddit r/{subreddit_name}: Found {subreddit_tips} tips (from {len(entries)} posts)")

                except ET.ParseError as e:
                    print(f"⚠️  Reddit r/{subreddit_name}: RSS parse error - {str(e)[:30]}")

            elif response.status_code == 429:
                print(f"⚠️  Reddit r/{subreddit_name}: Rate limited, skipping...")
            else:
                print(f"⚠️  Reddit r/{subreddit_name}: HTTP {response.status_code}")

        except Exception as e:
            print(f"⚠️  Reddit r/{subreddit_name}: Error - {str(e)[:50]}")

    print(f"🤖 Reddit: Total {len(tips)} tips found")
    return tips


def categorize_by_keywords(tips: list) -> list:
    """Fallback categorization using keywords when Gemini is unavailable."""
    categorized = []
    for tip in tips:
        content = (tip.get("content", "") + " " + tip.get("title", "")).lower()
        category = "workflow"  # default

        # Check each category's keywords
        for cat, keywords in CONFIG["category_keywords"].items():
            if any(kw in content for kw in keywords):
                category = cat
                break

        tip["category"] = category
        tip["ai_title"] = tip.get("title", "Tip")[:60]
        tip["summary"] = tip.get("content", "")[:200]
        categorized.append(tip)

    print(f"📂 Keyword categorization: {len(categorized)} tips categorized")
    return categorized


def validate_and_categorize(tips: list) -> list:
    """
    Use Gemini AI to validate tips and assign categories.

    Requires GEMINI_API_KEY environment variable.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not tips:
        return tips

    if not api_key:
        print("⚠️  Gemini: No API key found, using keyword categorization...")
        return categorize_by_keywords(tips)

    try:
        import google.generativeai as genai

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        validated_tips = []

        for tip in tips:
            prompt = f"""You are a STRICT content validator for Claude Code tips. Be very selective.

Content: {tip.get('content', '')[:500]}

VALID Claude Code tips MUST:
- Be about Claude Code CLI (the Anthropic terminal tool) or Claude Code workflows
- Contain actionable techniques, tricks, or patterns for using Claude Code
- Include specific commands, configurations, or methodologies

REJECT if content is:
- A bug report, question, or complaint
- About general Claude AI chat (not Claude Code CLI)
- About other AI tools (ChatGPT, Gemini, etc.)
- A product announcement or hiring post
- A general discussion without actionable advice
- About apps/tools built WITH Claude (not ABOUT Claude Code)

Tasks:
1. Is this a VALID Claude Code tip? (true ONLY if it's actionable advice about Claude Code CLI)
2. Rate quality 1-10 (be strict: 7+ only for genuinely useful tips)
3. Assign category: orchestration, context-management, workflow, subagents, or tooling
4. Write a concise title (max 60 chars)
5. Write a one-paragraph summary of the actionable tip

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

                # STRICT: Must be valid AND quality >= 7
                if result.get("is_valid") and result.get("quality", 0) >= 7:
                    tip["category"] = result.get("category", "workflow")
                    tip["ai_title"] = result.get("title", tip["title"])
                    tip["summary"] = result.get("summary", "")
                    tip["quality"] = result.get("quality", 5)
                    validated_tips.append(tip)
                else:
                    # Log rejected tips for debugging
                    print(f"   ❌ Rejected: {tip.get('title', 'Unknown')[:40]}... (valid={result.get('is_valid')}, quality={result.get('quality')})")

            except Exception as e:
                print(f"⚠️  Gemini validation error: {str(e)[:30]}")
                # Do NOT add tips that fail validation - skip them

        print(f"✨ Gemini: Validated {len(validated_tips)}/{len(tips)} tips")
        return validated_tips

    except ImportError:
        print("⚠️  Gemini: google-generativeai not installed, using keyword categorization...")
        return categorize_by_keywords(tips)


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


def append_tip_to_category(tip: dict, tip_number: int) -> bool:
    """Append a new tip to the category markdown file.

    Format:
    ## N. Tip Title
    **Source:** Author Name

    Content...

    ---
    """
    category = tip.get("category", "workflow")
    category_file = Path(f"tips/categories/{category}.md")

    if not category_file.exists():
        print(f"⚠️  Category file not found: {category_file}")
        return False

    # Read existing content
    content = category_file.read_text()

    # Find the last tip entry (before the footer)
    footer_marker = "*[Back to Categories]"

    # Create new tip entry
    new_tip = f"""
## {tip_number}. {tip.get('ai_title', tip.get('title', 'New Tip'))}
**Source:** {tip.get('author', 'Community')} ({tip.get('source', 'community').title()})

{tip.get('summary', tip.get('content', '')[:300])}

[Original]({tip.get('url', '#')}) | Added: {datetime.now().strftime('%Y-%m-%d')}

---
"""

    # Insert before footer or append at end
    if footer_marker in content:
        parts = content.split(footer_marker)
        new_content = parts[0] + new_tip + "\n" + footer_marker + parts[1]
    else:
        new_content = content.rstrip() + "\n" + new_tip

    category_file.write_text(new_content)
    print(f"✅ Added tip #{tip_number} to {category}.md")
    return True


def update_index(new_tips: list):
    """Update the tips/index.json file."""
    index_file = Path("tips/index.json")

    if index_file.exists():
        with open(index_file) as f:
            index = json.load(f)
    else:
        index = {"categories": [], "totalTips": 0, "lastUpdated": ""}

    # Update counts (case-insensitive category matching)
    for tip in new_tips:
        category = tip.get("category", "workflow").lower()
        # Find existing category (case-insensitive) - use slug for matching
        cat_entry = next(
            (c for c in index["categories"] if c.get("slug", c["name"]).lower() == category),
            None
        )
        if cat_entry:
            cat_entry["count"] = cat_entry.get("count", 0) + 1
        # Don't create new categories - only update existing ones

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
    tip_number = existing.get("next_number", 51)

    added_count = 0
    for tip in tips:
        if append_tip_to_category(tip, tip_number):
            added_count += 1
            tip_number += 1

    # Update index
    update_index(tips)

    # Update README
    update_readme_today_tip(tips)

    print(f"✅ Added {added_count} new tips to category files")


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
