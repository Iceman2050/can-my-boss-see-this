# can-my-boss-see-this

**You pasted customer data into ChatGPT on your work account. Can your boss read it?**

Most employees have no idea what workspace admins can see — custom instructions, memory, chat history, usage stats. This tool answers the question per platform and plan, from a researched visibility matrix.

## 30-second quickstart
```
python can_my_boss_see_this.py chatgpt enterprise
```

## Example output
```
{
  "platform": "chatgpt",
  "plan": "enterprise",
  "rows": [
    {
      "category": "Saved instructions / system prompts",
      "you_use_it": false,
      "admin_can_see": "yes",
      "note": "Workspace admins can retrieve your custom instructions via the admin console and audit logs."
    },
    {
      "category": "Memory / saved info",
      "you_use_it": false,
      "admin_can_see": "yes",
      "note": "Saved memories are visible to admins on Enterprise workspaces."
    },
    {
      "category": "Chat history content",
      "you_use_it": false,
      "admin_can_see": "yes",
      "note": "Conversation content is accessible to admins for compliance review."
    }
  ]
}
```

Platforms: `chatgpt | claude | gemini | copilot`. Add `--uses "customer data"` to check your specific data types.

## What it does NOT do
Policy research, not a live audit of your workspace. Admin capabilities change; verify against your provider's current docs before acting on it.

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



> Built by Ingenious AI with Muse — get free tokens with invite code `2HCQH1`
