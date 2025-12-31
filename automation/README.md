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
2. **Reddit RSS** fetches from r/ClaudeAI (public, no auth needed)
3. **Keyword Filter** pre-filters content (positive + negative keywords)
4. **Gemini AI** validates and categorizes tips (strict criteria)
5. **Deduplication** removes existing tips
6. **Repository Update** adds new tips to markdown files

### Data Sources

| Source | Method | Status |
|--------|--------|--------|
| Reddit | RSS Feed (public) | ✅ Primary |
| Twitter/X | API v2 | ❌ Requires $100/mo Basic tier |

### Filtering Pipeline

```
Reddit RSS → Keyword Filter → Gemini Validation → Dedupe → Commit
                  ↓                    ↓
           +25 negative          Quality >= 7
            keywords             STRICT criteria
```

### AI Curation

Gemini AI (gemini-2.0-flash) validates with strict criteria:

**VALID tips must:**
- Be about Claude Code CLI (not general Claude chat)
- Contain actionable techniques or patterns
- Include specific commands or methodologies

**REJECTED content:**
- Bug reports, questions, complaints
- Other AI tools (ChatGPT, Gemini, etc.)
- App showcases (built WITH Claude, not ABOUT Claude Code)
- General discussions without actionable advice

## Setup

### Required Secrets

Set these in your GitHub repository settings:

| Secret | Required | Description |
|--------|----------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key |
| `TWITTER_BEARER_TOKEN` | ⚠️ Optional | Twitter API v2 (needs Basic tier) |

### Getting API Keys

1. **Gemini**: [aistudio.google.com](https://aistudio.google.com) (free)
2. **Twitter**: [developer.twitter.com](https://developer.twitter.com) ($100/mo for search)

## Manual Trigger

```bash
# Via GitHub CLI
gh workflow run daily-update.yml

# Check status
gh run list --limit 3
```

Or via GitHub UI: Actions → Daily Update → Run workflow

## Local Development

```bash
# Set environment variable
export GEMINI_API_KEY="your-key"

# Run locally
cd /path/to/claude-code-daily
python automation/daily-update.py
```

## Graceful Degradation

The script handles missing credentials gracefully:
- Missing Gemini key → Falls back to keyword categorization
- Missing Twitter token → Skips Twitter (logged)
- Reddit RSS always works (public, no auth)
