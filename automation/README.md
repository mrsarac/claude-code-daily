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
3. **Reddit Scraper** fetches from r/ClaudeAI
4. **Gemini AI** validates and categorizes tips
5. **Deduplication** removes existing tips
6. **Repository Update** adds new tips to markdown files

### Data Sources

| Source | What We Look For |
|--------|------------------|
| Twitter/X | #ClaudeCode, #ClaudeDev hashtags |
| Reddit | r/ClaudeAI posts with 20+ upvotes |

### AI Curation

Gemini AI performs:
- **Validation**: Is this actually a Claude Code tip?
- **Categorization**: Which of the 5 categories?
- **Quality Check**: Is it specific and actionable?

## Setup

### Required Secrets

Set these in your GitHub repository settings:

```
TWITTER_BEARER_TOKEN    # Twitter API v2 bearer token
REDDIT_CLIENT_ID        # Reddit app client ID
REDDIT_CLIENT_SECRET    # Reddit app client secret
GEMINI_API_KEY          # Google Gemini API key
```

### Getting API Keys

1. **Twitter**: [developer.twitter.com](https://developer.twitter.com)
2. **Reddit**: [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
3. **Gemini**: [makersuite.google.com](https://makersuite.google.com)

## Manual Trigger

You can manually run the workflow:

1. Go to Actions tab
2. Select "Daily Update"
3. Click "Run workflow"

## Local Development

```bash
# Set environment variables
export TWITTER_BEARER_TOKEN="your-token"
export REDDIT_CLIENT_ID="your-id"
export REDDIT_CLIENT_SECRET="your-secret"
export GEMINI_API_KEY="your-key"

# Run locally
python automation/daily-update.py
```
