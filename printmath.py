#!/usr/bin/env python3
"""Minimal test script: print numbers 1..N (default N=5).

Usage:
  python printmath.py --count 5
"""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Minimal test script: print numbers 1..N")
    parser.add_argument("--count", "-n", type=int, default=5, help="How many numbers to print (default 5)")
    args = parser.parse_args(argv)

    if args.count < 0:
        print("count must be >= 0")
        return 2

    for i in range(1, args.count + 1):
        print(i)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
