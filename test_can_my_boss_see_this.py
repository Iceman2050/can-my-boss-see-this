"""Tests for can_my_boss_see_this (pure matrix logic)."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from can_my_boss_see_this import audit, VISIBILITY_MATRIX  # noqa: E402

PASS, FAIL = [], []


def check(name, fn):
    try:
        fn()
        PASS.append(name)
        print("PASS  " + name)
    except Exception as e:  # noqa: BLE001
        FAIL.append((name, repr(e)))
        print("FAIL  %s: %r" % (name, e))


def t_claude_enterprise_instructions_exposed():
    r = audit("claude", "enterprise", {"saved_instructions": True})
    row = [x for x in r["rows"] if x["category"].startswith("Saved")][0]
    assert row["admin_can_see"] == "yes"
    assert "Compliance API" in row["note"]
    assert "Saved instructions" in r["exposed_categories"][0]


def t_personal_plan_nothing_exposed():
    r = audit("claude", "pro", {"saved_instructions": True, "memory": True,
                                "chat_history": True})
    assert r["exposed_categories"] == []
    assert "none of the categories" in r["summary"]


def t_chatgpt_enterprise_memory_exposed():
    r = audit("chatgpt", "enterprise", {"memory": True})
    assert "Memory" in r["exposed_categories"][0]


def t_unknown_platform_errors():
    try:
        audit("notareal", "enterprise", {})
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def t_unknown_plan_errors():
    try:
        audit("claude", "notaplan", {})
    except ValueError:
        return
    raise AssertionError("expected ValueError")


def t_no_usage_declared():
    r = audit("gemini", "workspace", {})
    assert "no usage" in r["summary"].lower()


def t_disclaimer_present():
    r = audit("copilot", "m365", {"chat_history": True})
    assert "Not legal advice" in r["disclaimer"] or "not legal advice" in r["disclaimer"].lower()


def t_case_insensitive():
    r = audit("Claude", "Enterprise", {"memory": True})
    assert r["platform"] == "claude" and r["plan"] == "enterprise"


def t_matrix_covers_all_categories():
    cats = ("saved_instructions", "memory", "chat_history",
            "custom_gpts", "usage_stats")
    for plat, plans in VISIBILITY_MATRIX.items():
        for plan, matrix in plans.items():
            for c in cats:
                assert c in matrix, (plat, plan, c)
                assert matrix[c][0] in ("yes", "no", "aggregate", "unknown")


def test_all_checks():
    for name, fn in sorted(
            [(k, v) for k, v in globals().items() if k.startswith("t_")]):
        check(name, fn)
    print("\n%d passed, %d failed" % (len(PASS), len(FAIL)))
    assert not FAIL


if __name__ == "__main__":
    test_all_checks()
