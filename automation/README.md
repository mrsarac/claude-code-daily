# Automation

This directory contains the automation scripts for Claude Code Daily.

## Overview

```
automation/
├── daily-update.py   # Main automation script
└── README.md         # This file
```

## How It Works

### Daily Workflow

1. **GitHub Actions** triggers at 00:00 UTC daily
2. **Twitter Scraper** fetches posts with #ClaudeCode
3. **Reddit Scraper** fetches from r/ClaudeAI (optional)
4. **Gemini AI** validates and categorizes tips
5. **Deduplication** removes existing tips
6. **Repository Update** adds new tips to markdown files

### Data Sources

| Source | What We Look For | Status |
|--------|------------------|--------|
| Twitter/X | #ClaudeCode, #ClaudeDev hashtags | ✅ Active |
| Reddit | r/ClaudeAI posts with 20+ upvotes | ⚡ Optional |

> **Note:** The automation works with Twitter-only mode. Reddit integration is optional and can be enabled by adding Reddit API credentials.

### AI Curation

Gemini AI performs:
- **Validation**: Is this actually a Claude Code tip?
- **Categorization**: Which of the 5 categories?
- **Quality Check**: Is it specific and actionable?

## Setup

### Required Secrets

Set these in your GitHub repository settings:

| Secret | Required | Description |
|--------|----------|-------------|
| `TWITTER_BEARER_TOKEN` | ✅ Yes | Twitter API v2 bearer token |
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key |
| `REDDIT_CLIENT_ID` | ⚡ Optional | Reddit app client ID |
| `REDDIT_CLIENT_SECRET` | ⚡ Optional | Reddit app client secret |

### Getting API Keys

1. **Twitter**: [developer.twitter.com](https://developer.twitter.com)
2. **Gemini**: [aistudio.google.com](https://aistudio.google.com)
3. **Reddit** (optional): [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
   - Create a "script" type application
   - Copy the client ID (under app name) and secret

## Manual Trigger

You can manually run the workflow:

1. Go to Actions tab
2. Select "Daily Update"
3. Click "Run workflow"

## Local Development

```bash
# Set environment variables (Reddit is optional)
export TWITTER_BEARER_TOKEN="your-token"
export GEMINI_API_KEY="your-key"

# Optional: Reddit integration
export REDDIT_CLIENT_ID="your-id"
export REDDIT_CLIENT_SECRET="your-secret"

# Run locally
python automation/daily-update.py
```

## Graceful Degradation

The script handles missing credentials gracefully:
- Missing Twitter token → Skips Twitter, logs warning
- Missing Reddit credentials → Skips Reddit, logs warning
- Missing Gemini key → Skips AI validation, passes tips through

This means the automation will run successfully even with partial configuration.
