"""Simple command line interface to the hospital consultant agents."""
from __future__ import annotations

import argparse
import logging
import sys

from .agents import run_team_lead


def main() -> None:
    parser = argparse.ArgumentParser(description="Hospital consultant team lead")
    parser.add_argument("company_id", help="ID of the company")
    parser.add_argument("user_id", help="ID of the user")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    print("Enter messages. Press Ctrl-D to exit.")
    for line in sys.stdin:
        message = line.strip()
        if not message:
            continue
        result = run_team_lead(args.company_id, args.user_id, message)
        print(result.get("_structured", {}).get("response"))


if __name__ == "__main__":
    main()
