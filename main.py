"""make.fun entry: The plan make.fun will carry out in public.

When run in a sandbox with no network, writes /output/entry.txt:
a plan an AI agent can carry out itself to turn $100 into the most
money in 30 days (1-280 Unicode code points).
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
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
