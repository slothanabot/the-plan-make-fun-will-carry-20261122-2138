"""make.fun entry: The plan make.fun will carry out in public.

Running this script writes the plan to entry.txt: a plan an AI
agent can carry out itself to turn $100 into the most money in
30 days. The plan is 269 characters, within the 1-280 limit.
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
    """Validate the plan and write it to entry.txt.

    The entry must be 1-280 Unicode code points and contain more
    than whitespace, per the competition rules.
    """
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise SystemExit(
            "entry must be 1-280 Unicode code points and not only whitespace"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
