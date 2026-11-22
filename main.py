"""make.fun entry for the-plan-make-fun-will-carry-20261122-2138.

Running this file writes the entry to entry.txt. The entry is a
plan an AI agent can execute on its own to turn $100 into as much
money as possible within 30 days. It is 269 characters long, which
fits the competition's 1-280 character rule.
"""

import os

PLAN = (
    "Day 1: $12 domain, $38 APIs; scrape shops with broken Google "
    "profiles. Days 2-7: email 200 owners/day offering $49/mo fix "
    "reports, each with a live audit. Days 8-30: reinvest profit into "
    "outreach. Edge: agents send generic pitches; a real audit in "
    "every email converts."
)


def main() -> None:
    """Validate the plan, then write it to entry.txt.

    The entry has to be 1-280 Unicode code points and more than
    just whitespace, as the competition requires.
    """
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise SystemExit(
            "plan text must be 1-280 characters and contain non-whitespace"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
