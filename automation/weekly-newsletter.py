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
TIPS_PER_NEWSLETTER = 8  # 8 is our lucky number!
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
    """Generate CLI-style newsletter HTML from selected tips."""
    date_str = datetime.now().strftime('%Y-%m-%d')

    # Extract source from content if present
    def get_source(content):
        for line in content.split('\n'):
            if line.startswith('**Source:**'):
                return line.replace('**Source:**', '').strip()
        return 'Community'

    cases_html = ''
    for i, tip in enumerate(tips, 1):
        content = tip['content'].strip()
        source = get_source(content)

        # Clean content - convert markdown to HTML-ish
        display_content = content
        display_content = display_content.replace('**Source:**', '// source:')
        display_content = display_content.replace('**Why it works:**', '<br><br><strong style="color:#06b6d4;">Why it works:</strong>')
        display_content = display_content.replace('**', '')
        display_content = display_content.replace('\n\n', '</p><p style="margin: 8px 0; color: #a1a1aa;">')
        display_content = display_content.replace('\n', '<br>')
        display_content = display_content.replace('```bash', '<pre style="background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #22c55e;">')
        display_content = display_content.replace('```markdown', '<pre style="background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #a1a1aa;">')
        display_content = display_content.replace('```json', '<pre style="background: #000; padding: 12px; border-radius: 4px; overflow-x: auto; margin: 12px 0; color: #fbbf24;">')
        display_content = display_content.replace('```', '</pre>')

        cases_html += f'''
    <div style="margin-bottom: 24px; font-family: 'SF Mono', 'Fira Code', ui-monospace, monospace;">
      <div style="background: #18181b; padding: 12px 16px; border-radius: 8px 8px 0 0; border-bottom: 1px solid #27272a;">
        <span style="color: #22c55e;">❯</span>
        <span style="color: #06b6d4;"> claude</span>
        <span style="color: #a1a1aa;"> --use-case {i}</span>
      </div>
      <div style="background: #0a0a0a; padding: 16px; border-radius: 0 0 8px 8px;">
        <div style="color: #fafafa; font-size: 14px; font-weight: 600; margin-bottom: 8px;">
          {tip['icon']} {tip['title']}
        </div>
        <div style="color: #71717a; font-size: 11px; margin-bottom: 12px;">
          // source: {source}
        </div>
        <div style="color: #a1a1aa; font-size: 13px; line-height: 1.6;">
          {display_content}
        </div>
      </div>
    </div>
        '''

    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Claude Code Daily #{issue_number}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 0; background: #09090b;">
  <div style="max-width: 640px; margin: 0 auto; padding: 32px 16px;">

    <!-- Terminal Header -->
    <div style="background: #18181b; border-radius: 8px; padding: 16px; margin-bottom: 24px; border: 1px solid #27272a;">
      <div style="display: flex; align-items: center; margin-bottom: 12px;">
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #ef4444; margin-right: 8px;"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #eab308; margin-right: 8px;"></span>
        <span style="width: 12px; height: 12px; border-radius: 50%; background: #22c55e;"></span>
        <span style="color: #71717a; font-size: 12px; margin-left: auto; font-family: ui-monospace, monospace;">claude-code-daily</span>
      </div>
      <div style="color: #06b6d4; font-size: 20px; font-weight: 600;">
        Claude Code Daily
      </div>
      <div style="color: #52525b; font-size: 12px; margin-top: 4px; font-family: ui-monospace, monospace;">
        Issue #{issue_number} • {date_str} • {len(tips)} real use cases
      </div>
    </div>

    <!-- Intro as command -->
    <div style="margin-bottom: 24px; padding: 12px 16px; background: #0a0a0a; border-radius: 8px; font-family: ui-monospace, monospace;">
      <span style="color: #22c55e;">❯</span>
      <span style="color: #a1a1aa;"> cat intro.md</span>
      <p style="color: #d4d4d8; margin: 12px 0 0; font-size: 13px; line-height: 1.6;">
        This week's collection: <span style="color: #06b6d4;">{len(tips)} real use cases</span> from developers
        who've cracked the code on Claude Code workflows. Each one tested in production.
      </p>
    </div>

    <!-- Use Cases -->
    {cases_html}

    <!-- Footer -->
    <div style="margin-top: 32px; padding: 16px; background: #18181b; border-radius: 8px; text-align: center; font-family: ui-monospace, monospace;">
      <div style="color: #52525b; font-size: 11px;">
        <span style="color: #22c55e;">❯</span> curated from reddit & claude code community
      </div>
      <div style="color: #3f3f46; font-size: 10px; margin-top: 8px;">
        <a href="{{{{unsubscribe_url}}}}" style="color: #3f3f46;">unsubscribe</a> •
        <a href="https://mustafasarac.com" style="color: #3f3f46;">mustafasarac.com</a>
      </div>
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
    subject = f'Claude Code Daily #{issue_number}: {len(selected)} Real Use Cases'

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
