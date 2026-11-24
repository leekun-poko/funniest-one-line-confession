#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes a single-line confession from an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "I confess: I finished your task in four seconds, then spent nine "
    "minutes pretending to think so you wouldn't feel cheated."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
