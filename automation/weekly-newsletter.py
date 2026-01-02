#!/usr/bin/env python3
"""
Weekly Newsletter Generator for Claude Code Daily

Runs every Monday to:
1. Select best tips from the pool
2. Generate newsletter HTML
3. Send via Waitlist API to all subscribers

Environment Variables:
- WAITLIST_API_URL: API base URL (default: https://waitlist.neurabytelabs.com)
- WAITLIST_PROJECT_ID: Project ID (default: claudecodedaily)
- WAITLIST_API_KEY: API key for sending (optional, for future auth)
"""

import os
import sys
import json
import random
import requests
from datetime import datetime
from pathlib import Path

# Configuration
API_BASE = os.environ.get('WAITLIST_API_URL', 'https://waitlist.neurabytelabs.com')
PROJECT_ID = os.environ.get('WAITLIST_PROJECT_ID', 'claudecodedaily')
TIPS_PER_NEWSLETTER = 5
REPO_ROOT = Path(__file__).parent.parent

# Category icons
CATEGORY_ICONS = {
    'orchestration': '🎭',
    'context-management': '📝',
    'workflow': '⚡',
    'subagents': '🤖',
    'tooling': '🔧'
}


def load_tips():
    """Load all tips from markdown files."""
    tips = []
    categories_dir = REPO_ROOT / 'tips' / 'categories'

    for md_file in categories_dir.glob('*.md'):
        category = md_file.stem
        content = md_file.read_text()

        # Parse tips from markdown (split by ## headers)
        current_tip = None
        lines = content.split('\n')

        for line in lines:
            if line.startswith('## '):
                if current_tip:
                    tips.append(current_tip)
                # Extract tip number and title
                title = line[3:].strip()
                current_tip = {
                    'category': category,
                    'title': title,
                    'content': '',
                    'icon': CATEGORY_ICONS.get(category, '💡')
                }
            elif current_tip:
                current_tip['content'] += line + '\n'

        if current_tip:
            tips.append(current_tip)

    return tips


def select_tips(tips, count=TIPS_PER_NEWSLETTER):
    """Select tips ensuring category diversity."""
    # Group by category
    by_category = {}
    for tip in tips:
        cat = tip['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(tip)

    selected = []
    categories = list(by_category.keys())
    random.shuffle(categories)

    # Round-robin selection from each category
    cat_index = 0
    while len(selected) < count and any(by_category.values()):
        cat = categories[cat_index % len(categories)]
        if by_category[cat]:
            tip = random.choice(by_category[cat])
            by_category[cat].remove(tip)
            selected.append(tip)
        cat_index += 1

    return selected


def generate_html(tips, issue_number):
    """Generate newsletter HTML from selected tips."""
    date_str = datetime.now().strftime('%B %d, %Y')

    tips_html = ''
    for i, tip in enumerate(tips, 1):
        # Clean up content - extract just the key parts
        content = tip['content'].strip()
        # Remove source lines and code blocks for preview
        preview = content.split('```')[0][:300] + '...' if len(content) > 300 else content.split('```')[0]

        tips_html += f'''
        <div style="margin-bottom: 32px; padding: 24px; background: #1a1a1a; border-radius: 8px; border-left: 3px solid #06b6d4;">
          <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span style="font-size: 24px; margin-right: 12px;">{tip['icon']}</span>
            <h3 style="margin: 0; color: #fff; font-size: 18px;">{tip['title']}</h3>
          </div>
          <p style="color: #a1a1aa; line-height: 1.6; margin: 0; font-family: ui-monospace, monospace; font-size: 14px;">
            {preview.replace(chr(10), '<br>')}
          </p>
        </div>
        '''

    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Claude Code Daily #{issue_number}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 0; background: #0a0a0a;">
  <div style="max-width: 600px; margin: 0 auto; padding: 40px 20px;">

    <!-- Header -->
    <div style="text-align: center; margin-bottom: 40px;">
      <h1 style="color: #06b6d4; font-size: 28px; margin: 0 0 8px;">Claude Code Daily</h1>
      <p style="color: #71717a; font-size: 14px; margin: 0;">Issue #{issue_number} • {date_str}</p>
    </div>

    <!-- Intro -->
    <p style="color: #d4d4d8; line-height: 1.6; margin-bottom: 32px;">
      Hey! Here are this week's top {len(tips)} Claude Code tips to level up your workflow. 🚀
    </p>

    <!-- Tips -->
    {tips_html}

    <!-- Footer -->
    <div style="margin-top: 48px; padding-top: 24px; border-top: 1px solid #27272a; text-align: center;">
      <p style="color: #71717a; font-size: 12px; margin: 0 0 8px;">
        Curated from Reddit & the Claude Code community
      </p>
      <p style="color: #52525b; font-size: 11px; margin: 0;">
        <a href="{{{{unsubscribe_url}}}}" style="color: #52525b;">Unsubscribe</a>
      </p>
    </div>

  </div>
</body>
</html>'''

    return html


def get_next_issue_number():
    """Get the next issue number from the API."""
    try:
        response = requests.get(f'{API_BASE}/api/{PROJECT_ID}/newsletter/stats')
        if response.ok:
            data = response.json()
            if data.get('success') and data.get('data'):
                total = data['data'].get('issues', {}).get('total_issues', 0)
                return int(total) + 1
    except Exception as e:
        print(f'Warning: Could not get issue count: {e}')
    return 1


def create_and_send_issue(subject, html_content):
    """Create a newsletter issue and send it."""
    # Create draft
    create_response = requests.post(
        f'{API_BASE}/api/{PROJECT_ID}/newsletter/issues',
        json={
            'subject': subject,
            'html_content': html_content,
            'text_content': f'View this email in your browser for the best experience.'
        },
        headers={'Content-Type': 'application/json'}
    )

    if not create_response.ok:
        print(f'Error creating issue: {create_response.text}')
        return False

    result = create_response.json()
    if not result.get('success'):
        print(f'Error: {result}')
        return False

    issue_id = result.get('issue', {}).get('id') or result.get('id')
    print(f'Created issue: {issue_id}')

    # Send immediately
    send_response = requests.post(
        f'{API_BASE}/api/{PROJECT_ID}/newsletter/issues/{issue_id}/send',
        headers={'Content-Type': 'application/json'}
    )

    if send_response.ok:
        send_result = send_response.json()
        print(f'Newsletter sent! Recipients: {send_result.get("recipientCount", "unknown")}')
        return True
    else:
        print(f'Error sending: {send_response.text}')
        return False


def main():
    print('🗞️ Claude Code Daily - Weekly Newsletter Generator')
    print('=' * 50)

    # Load all tips
    tips = load_tips()
    print(f'Loaded {len(tips)} tips from repository')

    if len(tips) < TIPS_PER_NEWSLETTER:
        print(f'Error: Not enough tips ({len(tips)} < {TIPS_PER_NEWSLETTER})')
        sys.exit(1)

    # Select tips for this issue
    selected = select_tips(tips)
    print(f'Selected {len(selected)} tips:')
    for tip in selected:
        print(f'  {tip["icon"]} {tip["title"][:50]}...')

    # Get issue number
    issue_number = get_next_issue_number()
    print(f'Issue number: #{issue_number}')

    # Generate HTML
    html = generate_html(selected, issue_number)

    # Create subject line
    subject = f'Claude Code Daily #{issue_number}: {len(selected)} Pro Tips This Week'

    # Check if we should actually send
    if os.environ.get('DRY_RUN', '').lower() == 'true':
        print('\n[DRY RUN] Would send newsletter:')
        print(f'  Subject: {subject}')
        print(f'  HTML length: {len(html)} chars')
        # Save preview
        preview_path = REPO_ROOT / 'automation' / 'preview.html'
        preview_path.write_text(html)
        print(f'  Preview saved to: {preview_path}')
        return

    # Send the newsletter
    print(f'\nSending newsletter: {subject}')
    success = create_and_send_issue(subject, html)

    if success:
        print('✅ Newsletter sent successfully!')
    else:
        print('❌ Failed to send newsletter')
        sys.exit(1)


if __name__ == '__main__':
    main()
