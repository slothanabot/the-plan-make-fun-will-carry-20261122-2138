"""Write the 30-day $100-to-profit plan to ``entry.txt``.

The plan is a single fixed string.  This module validates it and writes
it to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (or ``/output/entry.txt`` when
the variable is unset), using UTF-8 with LF line endings.
"""

from __future__ import annotations

import os
import sys

# The plan, exactly as entered for the competition.
PLAN = (
    "Day 1: $12 domain, $38 APIs; scrape shops with broken Google "
    "profiles. Days 2-7: email 200 owners/day offering $49/mo fix "
    "reports, each with a live audit. Days 8-30: reinvest profit into "
    "outreach. Edge: agents send generic pitches; a real audit in "
    "every email converts."
)

MIN_LENGTH = 1
MAX_LENGTH = 280
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def validate_plan(text: str) -> str:
    """Return ``text`` unchanged if it is a usable plan, else fail loudly.

    A plan must be between 1 and 280 Unicode code points long and must
    contain at least one non-whitespace character.  Anything else is a
    data error, not something to silently truncate or pad.
    """
    if not text.strip():
        raise SystemExit("plan is empty or only whitespace")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        raise SystemExit(
            f"plan must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    return text


def resolve_output_dir() -> str:
    """Pick the directory for ``entry.txt`` from the environment.

    ``MAKEFUN_OUTPUT_DIR`` wins when set and non-empty; otherwise fall
    back to ``/output``.  The current directory is never used, so a
    stray run cannot litter the repo with an ``out`` folder.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return chosen


def write_entry(text: str, directory: str) -> str:
    """Write ``text`` to ``entry.txt`` inside ``directory``.

    The directory is created when missing and the file is written as
    UTF-8 with a single LF newline.  Returns the path that was written.

    Before touching the disk, the text is encoded to UTF-8 and decoded
    back; if the round trip ever changed a character, writing is
    refused rather than saving a corrupted plan.
    """
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise SystemExit("plan failed the UTF-8 round-trip check")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main(argv: list[str] | None = None) -> int:
    """Validate the plan and write it out; return a process exit code."""
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        raise SystemExit(f"unexpected arguments: {' '.join(argv)}")
    plan = validate_plan(PLAN)
    path = write_entry(plan, resolve_output_dir())
    print(f"wrote {len(plan)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
