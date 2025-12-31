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
from datetime import datetime, timedelta
from pathlib import Path

# Configuration
CONFIG = {
    "twitter": {
        "hashtags": ["#ClaudeCode", "#ClaudeDev"],
        "accounts": ["@anthropic", "@alexalbert__", "@AmandaAskell"],
        "min_likes": 10,
        "max_age_days": 7
    },
    "reddit": {
        "subreddits": ["ClaudeAI", "claudeai"],
        "min_score": 20,
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
    tips_file = Path("tips/index.json")
    if tips_file.exists():
        with open(tips_file) as f:
            return json.load(f)
    return {"tips": []}


def generate_tip_hash(tip_text: str) -> str:
    """Generate a hash for deduplication."""
    normalized = tip_text.lower().strip()
    return hashlib.md5(normalized.encode()).hexdigest()[:12]


def fetch_twitter_tips():
    """
    Fetch tips from Twitter/X.
    
    Requires TWITTER_BEARER_TOKEN environment variable.
    """
    token = os.getenv("TWITTER_BEARER_TOKEN")
    if not token:
        print("⚠️  Twitter: No bearer token found, skipping...")
        return []
    
    # TODO: Implement actual Twitter API v2 search
    # For now, return empty to avoid rate limits during testing
    print("🐦 Twitter: API integration pending...")
    return []


def fetch_reddit_tips():
    """
    Fetch tips from Reddit.
    
    Requires REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET.
    """
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("⚠️  Reddit: No credentials found, skipping...")
        return []
    
    # TODO: Implement actual PRAW integration
    print("🤖 Reddit: API integration pending...")
    return []


def validate_and_categorize(tips: list) -> list:
    """
    Use Gemini AI to validate tips and assign categories.
    
    Requires GEMINI_API_KEY environment variable.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("⚠️  Gemini: No API key found, skipping validation...")
        return tips
    
    # TODO: Implement Gemini validation
    print("✨ Gemini: Validation integration pending...")
    return tips


def deduplicate(new_tips: list, existing_tips: dict) -> list:
    """Remove tips that already exist in the repository."""
    existing_hashes = set()
    
    # Build hash set from existing tips
    for category in existing_tips.get("categories", []):
        for tip in category.get("tips", []):
            existing_hashes.add(generate_tip_hash(tip.get("title", "")))
    
    # Filter new tips
    unique_tips = []
    for tip in new_tips:
        tip_hash = generate_tip_hash(tip.get("title", ""))
        if tip_hash not in existing_hashes:
            unique_tips.append(tip)
            existing_hashes.add(tip_hash)
    
    return unique_tips


def update_readme_today_tip():
    """Update the 'Today's Tip' section in README."""
    # For now, rotate through existing tips
    # Later this will feature newly discovered tips
    print("📝 README: Today's Tip rotation pending...")


def update_repository(tips: list):
    """Add new tips to the appropriate category files."""
    if not tips:
        print("✅ No new tips to add today.")
        return
    
    print(f"📦 Adding {len(tips)} new tips...")
    # TODO: Implement file updates


def main():
    print("="*50)
    print(f"🚀 Claude Code Daily - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*50)
    
    # Load existing tips
    existing = get_existing_tips()
    print(f"📊 Existing tips: {existing.get('totalTips', 0)}")
    
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
    
    # Update Today's Tip
    update_readme_today_tip()
    
    print("="*50)
    print("✅ Daily update complete!")
    print("="*50)


if __name__ == "__main__":
    main()
