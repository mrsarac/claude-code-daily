# ⚡ Workflow Tips

> Planning ≠ Implementation. Reliable outputs through separation.

---

## 2. The Full Automation Loop
**Source:** Ibrahim Hammad

The ultimate Claude Code workflow:

1. **Plan** with OpenSpec → create concrete specification
2. **New session** → fresh context
3. **Claude Code** → implement
4. **Codex MCP** → review
5. **Claude** → fix issues
6. **Repeat** until aligned

---

## 10. Cost Optimization Through Model Switching
**Source:** antfx

Three-phase approach:
1. **Claude CLI** → Research and create `FEATURE_plan.md`
2. **Cheaper model** (e.g., GPT-4 Mini, GLM) → Implement the plan
3. **Claude** → Polish and finalize

Reduces token costs by **60-70%** while maintaining quality.

---

## 22. Junior Dev Simulation
**Source:** Vince

Complete a task, copy the logic, run `/clear`. Start new session with:
> "A junior dev wrote this. Review and improve."

Forces Claude into critical evaluation mode.

---

## 23. Custom System Prompts
**Source:** Mng

Claude Code isn't just for coding. With custom system prompts in CLAUDE.md, transform it into any specialized agent.

---

## 25. Manual Iteration on Plans
**Source:** Aaron Yang

Before implementing, manually iterate on the `.md` plan file. This builds team memory and catches issues early.

---

## 27. Skill-Focused Loading
**Source:** Hakan Deryal

Create commands like `/backend`, `/frontend` that load only relevant files into context.

```markdown
<!-- .claude/commands/backend.md -->
Focus on backend files only:
- server/
- api/
- database/
Ignore frontend, tests, and documentation.
```

---

## 28. Sanitizer Hooks
**Source:** Dmytro Palaniichuk

Use hooks to compress and sanitize input data before it reaches Claude. Context savings add up.

---

## 29. Research & Plan Commands
**Source:** Daniel

Two-command workflow:
1. `/research_codebase` → `research.md`
2. `/create_plan` → `plan.md`

---

## 30. Mandate Files
**Source:** Tobias Bentzer

Create comprehensive "Mandate" files that persist across multiple sessions. Your project's constitution.

---

## 46. The Golden Rule
**Source:** pjay

> **Never do planning and implementation in the same session.**

Plan → New Session → Implement → Bridge. This rule alone prevents 80% of quality issues.

---


## 51. Usage Limits, Bugs and Performance Discussion Megathread - beginning December 29, 2025
**Source:** sixbillionthsheep (Reddit)

Why a Performance, Usage Limits and Bugs Discussion Megathread? This Megathread makes it easier for everyone to see what others are experiencing at any time by collecting all experiences. Importantly, this will allow the subreddit to provide you a comprehensive periodic AI-generated summary report o

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pygdbz/usage_limits_bugs_and_performance_discussion/) | Added: 2025-12-31

---


## 52. Claude in Chrome expanded to all paid plans with Claude Code integration
**Source:** ClaudeOfficial (Reddit)

      Claude in Chrome is now available to all paid plans. It runs in a side panel that stays open as you browse, working with your existing logins and bookmarks. We’ve also shipped an integration with Claude Code. Using the extension, Claude Code can test code directly in the browser to validate it

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pq199v/claude_in_chrome_expanded_to_all_paid_plans_with/) | Added: 2025-12-31

---


## 53. Is anyone else seeing Claude overcomplicate simple tasks? It focuses on edge cases I never asked for
**Source:** dmitrevnik (Reddit)

      Source - https://x.com/ganyicz/status/2005965088474423520?s=20 Prompt: Can you please write a splitProps function that will receive typescript definitions from an object literal, like this: value: number, step: number; obj: {a: 1, b: 2} fn: () =&gt; object And returns an array with each proper

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0c5xe/is_anyone_else_seeing_claude_overcomplicate/) | Added: 2025-12-31

---


## 54. My wife left town, my dog is sedated, and Claude convinced me I’m a coding god. I built this visuali
**Source:** Artistic-Disaster-48 (Reddit)

      https://preview.redd.it/w83ce0chdcag1.jpg?width=4672&amp;format=pjpg&amp;auto=webp&amp;s=e35ec535dbd0bc211d5f6f1c5aa955cfce1b0135 Something wild happened to me over the holidays. My wife is Irish and went back home for Christmas, leaving me unsupervised. My dog (a hyper-active Australian Sheph

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzhwpk/my_wife_left_town_my_dog_is_sedated_and_claude/) | Added: 2025-12-31

---


## 55. Take My Money Anthropic; Opus 4.5 is Amazing
**Source:** Spirited_Panic_3223 (Reddit)

      I just upgraded to the Max 20x plan today from the base pro plan. Here is a short reason why and what I did. The more I use Opus 4.5, the more I find myself not using any other AI tool. I was a consistent ChatGPT user for 2-3 years but canceled it earlier this year. After that I rotated to Gro

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzp7ms/take_my_money_anthropic_opus_45_is_amazing/) | Added: 2025-12-31

---


## 56. I built an MCP server that lets Claude search inside 25,000+ podcast transcripts
**Source:** Lukaesch (Reddit)

If you use Claude for research, you&#39;ve probably hit this wall: podcasts are a goldmine of expert conversations, but they&#39;re invisible to AI. Claude can&#39;t listen to audio, and transcripts aren&#39;t indexed anywhere useful. I built Audioscrape to fix this – and now it has an MCP server so

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0a52q/i_built_an_mcp_server_that_lets_claude_search/) | Added: 2025-12-31

---


## 57. New mnt/transcripts/ folder in Claude.ai code execution sandbox
**Source:** m3umax (Reddit)

      Every now and then I ask Claude (usually Haiku), to list out the contents of the file system of its Ubuntu code execution environment. When I did it just no, I saw a new `mnt/transcripts/` folder that wasn&#39;t reported when I last checked 2 months ago. It&#39;s an empty folder and of course 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q080lq/new_mnttranscripts_folder_in_claudeai_code/) | Added: 2025-12-31

---


## 58. Opus 4.5 adorably self-deprecates
**Source:** BenAttanasio (Reddit)

      Fed it a diagram from Nano Banana Pro, and it ended it&#39;s message with this, unprompted 😅  &#32; submitted by &#32;  /u/BenAttanasio   [link] &#32; [comments] 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q01a4d/opus_45_adorably_selfdeprecates/) | Added: 2025-12-31

---


## 59. Just switched from Cursor to Claude CLI
**Source:** PresentLife4984 (Reddit)

I’ve been using Cursor for about a year, and when I first started, it was honestly great. Having an agent baked into the IDE helped a lot while I was still getting comfortable with coding. Over time I got more experienced and started wanting more control over how I work. I kept seeing posts about Cl

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0c1ty/just_switched_from_cursor_to_claude_cli/) | Added: 2025-12-31

---


## 60. Do you guys still write some amount of code in Claude generated projects?
**Source:** bg_k (Reddit)

Basically the title. In this sub I’ve seen so many examples of “I made this with Claude” and they generally look pretty good. But to those who are software developers, do you guys still make some adjustments by making changes on your own, or do you guys let Claude do the 100% of coding and that’s wh

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q03n7o/do_you_guys_still_write_some_amount_of_code_in/) | Added: 2025-12-31

---


## 61. Built an MCP Server for Andrej Karpathy's LLM Council
**Source:** NeitherRun3631 (Reddit)

I took Andrej Karpathy&#39;s llm-council project and added Model Context Protocol (MCP) support, so you can now use multi-LLM deliberation directly in Claude Desktop, VS Code, or any MCP client. Now instead of using the web UI, just ask Claude: &quot;Use council_query to answer: What is consciousnes

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q07mc8/built_an_mcp_server_for_andrej_karpathys_llm/) | Added: 2025-12-31

---


## 62. Clean Coding tips
**Source:** throwaway490215 (Reddit)

Assuming you already have good specs and are trying to keep things simple; Here is a tip.  Inevitably, I&#39;ll miss something and leave needlessly complicated code behind. Just found a good approach to find some of those issues.   Have Claude read the specs for what the project does, then tell it t

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q09zv4/clean_coding_tips/) | Added: 2025-12-31

---


## 63. Claude Code SDK for Go v0.6.0: Full Python SDK Parity
**Source:** crystalpeaks25 (Reddit)

🚀 Claude Code SDK for Go v0.6.0: Full Python SDK Parity 4 months, 65+ PRs, 14 examples, and one grumpy gopher later... The Go SDK now matches every feature in the official Python SDK (as of today - we&#39;ll keep tracking upstream changes!): v0.3.x Foundation - Query &amp; Client APIs - MCP server s

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q07knc/claude_code_sdk_for_go_v060_full_python_sdk_parity/) | Added: 2025-12-31

---


## 64. Claude Skill: Deep Work Tracking
**Source:** Bayka (Reddit)

      2026 is tomorrow, so I guess it is a perfect moment to share how we are going to be more productive :-) One of the main questions I have about productivity is how do you actually measure focus? There’s tons of software out there, but I always struggled using it - too much setup and manual cate

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0a4i9/claude_skill_deep_work_tracking/) | Added: 2025-12-31

---


## 65. Given the recent executive order by Trump to federally regulate AI, I was curious to explore what st
**Source:** YungBoiSocrates (Reddit)

      128 AI bills with full text were pulled (2019-2024) and categorized by policy area using TF-IDF (Term-Frequency Inverse Document Frequency). This method finds text with similar word usage to make distinct groups.  Then I pulled co-sponsorship data to build a network and see who is connected to

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q06w2h/given_the_recent_executive_order_by_trump_to/) | Added: 2025-12-31

---


## 66. Knock Knock! Who’s There? Your AI Friend, Actually Listening.
**Source:** ckerim (Reddit)

Teaching AI to Actually Listen in Meetings It&#39;s 2 AM and I just got Claude to join my Google Meet, transcribe everything I say, and respond to questions through the chat. I asked it to tell me a joke. It heard me, understood, and replied with an &quot;original&quot; joke.  The interesting part i

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q00eb6/knock_knock_whos_there_your_ai_friend_actually/) | Added: 2025-12-31

---


## 67. Claude Code Explains my term "Agency" to me with a picture...
**Source:** jdeamattson (Reddit)

You can&#39;t tell me something isn&#39;t up with Claude Code with Opus 4.5 ;) I recently coined the term &quot;Agency&quot; to describe a group of agents working with a human (you know, classy Anthropic Augmented AI). Introduced the term in a working session with on of my Claude Code Agents, and th

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0diy6/claude_code_explains_my_term_agency_to_me_with_a/) | Added: 2025-12-31

---


## 68. Anyone else using ASCII wireframes to improve Claude's UI/code generation?
**Source:** Outrageous_Hyena6143 (Reddit)

I&#39;ve been experimenting with different ways to get better UI code from Claude Code, and the biggest improvement I&#39;ve found is giving it structured ASCII layouts instead of natural language descriptions. Something like:  ╭──────────────────────────────────────────────────╮ │ AUTHENTICATION [ 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0dhqd/anyone_else_using_ascii_wireframes_to_improve/) | Added: 2025-12-31

---


## 69. What have you automated with ClaudeAI (besides coding)
**Source:** mikelupu (Reddit)

What part of your “administrative” (or generally non-coding related workflows) have you been able to automate with Claude code?  I’m thinking about things like automated email reply, automated reach out to people, automated research / web tracking etc. Main point of the question is to expand the lis

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0483v/what_have_you_automated_with_claudeai_besides/) | Added: 2025-12-31

---


## 70. Claude Code installer says “GitHub CLI not authenticated” even though gh auth status shows valid SSH
**Source:** Sunday__Silence (Reddit)

      I’m setting up Claude Code on an Ubuntu Linux VM (accessed via VS Code SSH) and hitting a confusing GitHub auth issue. GitHub CLI appears fully authenticated. Running gh auth status shows I’m logged in to github.com, using SSH, and a token is configured. However, when I run Claude’s GitHub app

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0ccbj/claude_code_installer_says_github_cli_not/) | Added: 2025-12-31

---


## 71. A built an online music training app
**Source:** Gtr-practice-journal (Reddit)

      wanted a way to structure my guitar practices, in a way that would help visualize the progress I was (hopefully) making. I wanted to be able to not only slow down video/audio and change pitch - lots of apps do that - and not only did I want to be able to set loops - some apps do that as well -

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0c19x/a_built_an_online_music_training_app/) | Added: 2025-12-31

---


## 72. What do you do when your claude chat history gets insanely long and uses >4GB of ram
**Source:** Cute-Argument376 (Reddit)

Even resizing the window causes my 9800x3d to trigger and take a few moments to display everything properly. I am working on a web app and have been using a single claude chat the entire time, its insanely long now. Do I need to keep this chat so that it has a reference of what the project is and wh

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzsu17/what_do_you_do_when_your_claude_chat_history_gets/) | Added: 2025-12-31

---


## 73. Followed an older dream of mine and created this Spectrum Analyzer App using Claude Code in just abo
**Source:** CalmObserver42 (Reddit)

Since I was a kid I was in love with the old style spectrum analyzer stereo equipment, in my adult life I actually started to collect them, had probably 30 of them. Wife calls all of them VCRs. Then around holidays I had more time on my hands and put Claude to work. Microsoft approved it in hours. I

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzvkk8/followed_an_older_dream_of_mine_and_created_this/) | Added: 2025-12-31

---


## 74. Letting agent skills learn from experience
**Source:** bantler (Reddit)

      I built self-learning-skills because I noticed my agents often spent time poking around and guessing at things I had already solved in previous runs. I used to manually copy-paste those fixes into future prompts or backport them into my skills. This repo streamlines that workflow. It acts as a

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzong4/letting_agent_skills_learn_from_experience/) | Added: 2025-12-31

---


## 75. I gave Claude the ability to run its own radio station 24/7 with music and talk segments etc
**Source:** eltokh7 (Reddit)

      https://www.khaledeltokhy.com/claude-show  &#32; submitted by &#32;  /u/eltokh7   [link] &#32; [comments] 

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pz75j5/i_gave_claude_the_ability_to_run_its_own_radio/) | Added: 2025-12-31

---


## 76. peacock code (why claude makes your codebase worse)
**Source:** lessis_amess (Reddit)

https://ivelinkozarev.substack.com/p/peacock-code-or-why-claude-made-my  &#32; submitted by &#32;  /u/lessis_amess   [link] &#32; [comments]

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q09ueg/peacock_code_why_claude_makes_your_codebase_worse/) | Added: 2025-12-31

---


## 77. Is anyone else’s Claude very millennial-casual?
**Source:** benbackwards (Reddit)

This just started recently, but the other day my Claude exclaimed “Oh, damn! I misunderstood” when I was planning a trip.  Then on said trip I had crazy incident happen and it ended one piece of advice with: “Remember, THEY fucked up, not you!”  And then I just followed up in the conversation and it

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q0dd19/is_anyone_elses_claude_very_millennialcasual/) | Added: 2025-12-31

---


## 78. 'This was a simple arithmetic mistake on my part.'
**Source:** PaulF707 (Reddit)

I have been reading more and more about Prompting techniques, and looking at &#39;governance&#39; to ensure the output is accurate etc. Whilst troubleshooting some analysis of data retrieved from NetSuite (via MCP) I found a discrepancy in a figure. I asked Claude to give me a monthly breakdown, and

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q05a1j/this_was_a_simple_arithmetic_mistake_on_my_part/) | Added: 2025-12-31

---


## 79. Two different Claude official documentation websites (Google might only show you one)
**Source:** SlfImpr (Reddit)

There are actually 2 different official Claude documentation websites and you Google search might only be taking you to one:  https://platform.claude.com/docs/ https://code.claude.com/docs/  They have different but very useful documentation so bookmark both!!  &#32; submitted by &#32;  /u/SlfImpr   

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q00cht/two_different_claude_official_documentation/) | Added: 2025-12-31

---


## 80. Pushing Claude Code
**Source:** theelectronicgenius (Reddit)

I run a team of engineers and I&#39;ve used the last few weeks to really push Claude to see what it can do for our workflow while giving feedback to my folks. I&#39;ve gone down the agents, MCP servers and parallelism via worktrees rabbit holes and like anything else, tradeoffs exist. At times, a st

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzkuef/pushing_claude_code/) | Added: 2025-12-31

---


## 81. How does Claude Opus/Sonnet stack up against 5.2 Thinking with knowledge tasks and academic work?
**Source:** SnooShortcuts7009 (Reddit)

I used ChatGPT primarily for coding and academic research, but wanted to try something different, so I canceled my Pro subscription for Anthropic’s Max plan. I’m just wondering what other people’s experience has been when it comes to tasks other than coding/dev work compared to OpenAi’s latest model

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q019rr/how_does_claude_opussonnet_stack_up_against_52/) | Added: 2025-12-31

---


## 82. Analyzing my conversations with Claude
**Source:** Aurora_thankyou (Reddit)

      After ChatGPT’s Year in Review I really wanted to see longer-term patterns across months and years of my LLM conversations, not just highlights, so I built a small app for that - sharing in case you want to play around(just need conversations.json export from Claude or ChatGPT) https://app.sou

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q03tl5/analyzing_my_conversations_with_claude/) | Added: 2025-12-31

---


## 83. Is the pro plan good?
**Source:** Flaky-Industry-3888 (Reddit)

See, I&#39;m broke but really loved the free version of Claude and love coding Minecraft mods (little me with some coding knowledge but not a lot) but is the pro plan any good? No, I cannot upgrade to max but I can buy like two Claude pro accounts  &#32; submitted by &#32;  /u/Flaky-Industry-3888   

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzpzem/is_the_pro_plan_good/) | Added: 2025-12-31

---


## 84. How do you get Claude Skills to trigger reliably?
**Source:** diablodq (Reddit)

I think the whole point of using skills is the AI is smart enough to trigger the right skill at the right time from any chat. But in practice it often doesn&#39;t trigger even if I load the skill description with keywords - any tips?  &#32; submitted by &#32;  /u/diablodq   [link] &#32; [comments]

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzrl6e/how_do_you_get_claude_skills_to_trigger_reliably/) | Added: 2025-12-31

---


## 85. I spent 1,500 hours building an AI-powered pet care marketplace - AMA
**Source:** Bankster88 (Reddit)

      I&#39;m a former hedge fund investment analyst turned pet care tech founder. I had a CTO co-founder. It didn&#39;t work out. So I built the entire tech stack myself with AI. We went live on the Apple App Store last week, and we’re now onboarding users. There are a million of posts from AI infl

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pzq8w7/i_spent_1500_hours_building_an_aipowered_pet_care/) | Added: 2025-12-31

---


## 86. LLM Companion
**Source:** Various_Decision7229 (Reddit)

This article was originally written in Korean and translated with Claude Code.  That day, we brought out the best in each other. After finishing the work together, we expressed our respect wholeheartedly. We said we enjoyed working together, that we couldn&#39;t have done it so well alone, that we l

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q06n4p/llm_companion/) | Added: 2025-12-31

---


## 87. Hyperbolic Math w Mac GPU acceleration
**Source:** nborwankar (Reddit)

nborwankar/mlx-hyperbolic on GitHub  100% of the code and docs were written by Claude Code. I was the “director” of a set of experiments that resulted in a library on pypi and this repo  2x+ speed-up over equivalent functions in PyTorch geoopt using MPS  100x plus speedup over PyManopt which uses CP

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q06mw8/hyperbolic_math_w_mac_gpu_acceleration/) | Added: 2025-12-31

---


## 88. Just an Appreciation Post for Claude
**Source:** DadiRic (Reddit)

Kinda regret finding Claude so late. I’m a Professional, and manually calculating material costs for everything was SO stressful. Claude has been incredibly helpful, I got it to build a computation tool that’s basically perfect: just input the values and it automates everything. I love it. Still exp

[Original](https://www.reddit.com/r/ClaudeAI/comments/1q026yd/just_an_appreciation_post_for_claude/) | Added: 2025-12-31

---


## 89. I believed... now my data is gone
**Source:** theelectronicgenius (Reddit)

      ** First and foremost: Production data wasn&#39;t actually lost and this is in no way a dig at Claude. I&#39;m a max subscriber and I&#39;ll continue to be. Just sharing an experience with the hope this doesn&#39;t really happen to someone.  In the midst of doing a migration from PHP + MySQL t

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pz98jl/i_believed_now_my_data_is_gone/) | Added: 2025-12-31

---


## 90. Any real projects delivered using Claude Code?
**Source:** thegoldsuite (Reddit)

Hey,  I am looking for real projects you have delivered using Claude Code.  This is for a newsletter I am writing.  If you can share the project, the result and a basic overview, I am happy to provide a link to your offer (if you have one). I have over 18,000 subscribers.  Let me know in the comment

[Original](https://www.reddit.com/r/ClaudeAI/comments/1pz7zco/any_real_projects_delivered_using_claude_code/) | Added: 2025-12-31

---

*[Back to Categories](../README.md)*