# can-my-boss-see-this

**Your AI workspace settings were written for an audience of one. They may have an audience of many.**

On 2026-10-15, Anthropic's release notes added a beta **Compliance API** letting Enterprise admins retrieve every member's saved "Instructions for Claude" and Cowork "Global instructions" (alfw.ai). Every existing visibility tool serves admins auditing employees. This one serves the employee.

`can-my-boss-see-this` takes the settings YOU declare (platform, plan, which categories you use) and produces a plain-English report of exactly what your employer/admin can read via admin APIs and logs — saved instructions, memory, chat history, custom GPTs/projects, usage stats.

## What it does NOT do
It never fetches anyone's real workspace data — it works from declared settings against a documented visibility matrix. It is not legal advice, and vendor admin capabilities change; verify against current documentation.

## Usage
```
python -m can_my_boss_see_this claude enterprise --uses saved_instructions,memory,chat_history
```

## Built by Ingenious AI

This tool is built and maintained by **Ingenious AI**. Get early access to our AI security platforms:

- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DisclosureGuard
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ModelMinder
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20TermsWatch
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Vibe-Code%20Audit
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Rogue-Agent%20Defense
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20BreachHunter
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ChatBreaker
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Flight%20Recorder
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20Agent%20Auth%20Gateway
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20DomainGuard
- https://wa.me/5016691053?text=Hi%20Ingenious%20AI!%20I%20want%20early%20access%20to%20ContentCraft%20AI

