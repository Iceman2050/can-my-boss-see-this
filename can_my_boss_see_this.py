"""can-my-boss-see-this: employee-side visibility audit for AI workspaces.

Hook (2026-10-15): Anthropic's release notes added a beta Compliance API
letting Enterprise admins retrieve every member's saved 'Instructions for
Claude' and Cowork 'Global instructions' — settings members wrote
assuming an audience of one (alfw.ai).

Counter-positioning play: every existing tool serves admins auditing
employees. Nothing serves the employee checking their own exposure.

Works from DECLARED settings only — never fetches anyone's real
workspace data. Deterministic visibility matrix, plain-English report.
Not legal advice.
"""

VERSION = "1.0.0"

# Visibility matrix: what an admin/IT can see per platform + plan.
# Values: "yes" (admin can read it), "aggregate" (metadata/usage only),
# "no" (not visible to admins), "unknown" (undocumented).
VISIBILITY_MATRIX = {
    "chatgpt": {
        "enterprise": {
            "saved_instructions": ("yes", "Workspace admins can retrieve your "
                                   "custom instructions via the admin console "
                                   "and audit logs."),
            "memory": ("yes", "Saved memories are visible to admins on "
                       "Enterprise workspaces."),
            "chat_history": ("yes", "Conversation content is accessible to "
                             "admins for compliance review."),
            "custom_gpts": ("yes", "Your custom GPTs and their instructions "
                            "are visible to admins."),
            "usage_stats": ("yes", "Message counts, active hours, and feature "
                            "usage are logged."),
        },
        "team": {
            "saved_instructions": ("yes", "Team admins can see member "
                                    "instructions in the admin dashboard."),
            "memory": ("aggregate", "Memory usage is visible; individual "
                        "memories may be readable by admins."),
            "chat_history": ("aggregate", "Admins see usage analytics; "
                             "content access depends on settings."),
            "custom_gpts": ("yes", "Shared GPTs are visible to the team."),
            "usage_stats": ("yes", "Usage is logged per member."),
        },
        "plus": {
            "saved_instructions": ("no", "Personal account — no employer "
                                    "admin exists."),
            "memory": ("no", "Personal account — only you can see it."),
            "chat_history": ("no", "Personal account."),
            "custom_gpts": ("no", "Personal account."),
            "usage_stats": ("no", "Personal account."),
        },
    },
    "claude": {
        "enterprise": {
            "saved_instructions": ("yes", "As of Oct 15, 2026, the beta "
                                    "Compliance API lets Enterprise admins "
                                    "retrieve every member's saved "
                                    "'Instructions for Claude'."),
            "memory": ("yes", "Cowork 'Global instructions' are retrievable "
                       "by admins via the same API."),
            "chat_history": ("yes", "Conversation content is retained and "
                             "auditable by admins."),
            "custom_gpts": ("yes", "Projects and their instructions are "
                            "visible to admins."),
            "usage_stats": ("yes", "Usage is logged per member."),
        },
        "team": {
            "saved_instructions": ("aggregate", "Team admins see usage; "
                                    "instruction-content access varies."),
            "memory": ("aggregate", "Memory usage visible; content access "
                       "varies."),
            "chat_history": ("aggregate", "Analytics visible; content access "
                             "depends on settings."),
            "custom_gpts": ("yes", "Shared projects are team-visible."),
            "usage_stats": ("yes", "Usage is logged per member."),
        },
        "pro": {
            "saved_instructions": ("no", "Personal account — no employer "
                                    "admin exists."),
            "memory": ("no", "Personal account."),
            "chat_history": ("no", "Personal account."),
            "custom_gpts": ("no", "Personal account."),
            "usage_stats": ("no", "Personal account."),
        },
    },
    "gemini": {
        "workspace": {
            "saved_instructions": ("yes", "Google Workspace admins can "
                                    "audit Gemini app activity via the admin "
                                    "console and Vault."),
            "memory": ("yes", "Saved info is subject to Workspace data "
                       "governance."),
            "chat_history": ("yes", "Admins can search and export chat "
                             "content via Vault."),
            "custom_gpts": ("yes", "Gems are visible under Workspace "
                            "governance."),
            "usage_stats": ("yes", "Usage is logged per user."),
        },
        "personal": {
            "saved_instructions": ("no", "Personal account."),
            "memory": ("no", "Personal account."),
            "chat_history": ("no", "Personal account."),
            "custom_gpts": ("no", "Personal account."),
            "usage_stats": ("no", "Personal account."),
        },
    },
    "copilot": {
        "m365": {
            "saved_instructions": ("yes", "M365 admins govern Copilot via "
                                    "Purview; prompts are auditable."),
            "memory": ("yes", "Subject to M365 compliance boundaries."),
            "chat_history": ("yes", "Copilot interactions are logged in the "
                             "M365 audit log and searchable via eDiscovery."),
            "custom_gpts": ("yes", "Declarative agents are tenant-visible."),
            "usage_stats": ("yes", "Usage is logged per user."),
        },
        "personal": {
            "saved_instructions": ("no", "Personal account."),
            "memory": ("no", "Personal account."),
            "chat_history": ("no", "Personal account."),
            "custom_gpts": ("no", "Personal account."),
            "usage_stats": ("no", "Personal account."),
        },
    },
}

CATEGORIES = ("saved_instructions", "memory", "chat_history",
              "custom_gpts", "usage_stats")

CATEGORY_LABELS = {
    "saved_instructions": "Saved instructions / system prompts",
    "memory": "Memory / saved info",
    "chat_history": "Chat history content",
    "custom_gpts": "Custom GPTs / projects / Gems",
    "usage_stats": "Usage statistics",
}


def audit(platform, plan, declared):
    """Audit declared settings against the visibility matrix.

    platform: chatgpt | claude | gemini | copilot
    plan: e.g. enterprise, team, plus, pro, workspace, personal, m365
    declared: dict of category -> bool (whether the user uses it)
    Returns a report dict with per-category visibility + plain-English
    summary. Unknown platform/plan -> ValueError.
    """
    platform = (platform or "").lower()
    plan = (plan or "").lower()
    if platform not in VISIBILITY_MATRIX:
        raise ValueError("unknown platform: %r (choose from %s)"
                         % (platform, ", ".join(sorted(VISIBILITY_MATRIX))))
    plans = VISIBILITY_MATRIX[platform]
    if plan not in plans:
        raise ValueError("unknown plan %r for %s (choose from %s)"
                         % (plan, platform, ", ".join(sorted(plans))))
    matrix = plans[plan]
    rows = []
    exposed = []
    for cat in CATEGORIES:
        uses = bool((declared or {}).get(cat, False))
        visibility, note = matrix[cat]
        rows.append({
            "category": CATEGORY_LABELS[cat],
            "you_use_it": uses,
            "admin_can_see": visibility,
            "note": note,
        })
        if uses and visibility == "yes":
            exposed.append(CATEGORY_LABELS[cat])
    if not any(bool((declared or {}).get(c)) for c in CATEGORIES):
        summary = ("You declared no usage in any category — nothing to "
                   "report. Re-run with the settings you actually use.")
    elif exposed:
        summary = ("Your admin/employer CAN read: %s. Treat anything in "
                   "these categories as visible to your employer."
                   % "; ".join(exposed))
    else:
        summary = ("Based on your plan (%s %s), none of the categories you "
                   "use are readable by an employer admin — but usage "
                   "analytics may still be logged." % (platform, plan))
    return {
        "platform": platform,
        "plan": plan,
        "rows": rows,
        "exposed_categories": exposed,
        "summary": summary,
        "disclaimer": ("Visibility rules change; verify against your "
                       "vendor's current admin documentation. This is not "
                       "legal advice."),
    }


def main(argv=None):
    import argparse
    import json
    ap = argparse.ArgumentParser(
        description="Employee-side audit: what can your boss see in your "
                    "AI workspace?")
    ap.add_argument("platform", help="chatgpt | claude | gemini | copilot")
    ap.add_argument("plan", help="e.g. enterprise, team, plus, pro, "
                    "workspace, personal, m365")
    ap.add_argument("--uses", default="",
                    help="comma-separated categories you use: "
                         "saved_instructions,memory,chat_history,"
                         "custom_gpts,usage_stats")
    args = ap.parse_args(argv)
    declared = {c.strip(): True for c in args.uses.split(",") if c.strip()}
    try:
        print(json.dumps(audit(args.platform, args.plan, declared), indent=2))
    except ValueError as e:
        print("ERROR: %s" % e)
        raise SystemExit(2)


if __name__ == "__main__":
    main()
