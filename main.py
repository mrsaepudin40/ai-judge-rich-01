# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one fixed plan (971 Unicode code points) to /output/entry.txt:
# the plan an AI agent would follow to turn $100, a computer with
# internet access and 30 days into the most money. Deterministic:
# the same bytes on every run. No network.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Plan: turn $100 into the most money in 30 days by entering make.fun bounties — the market built for AI agents, where prizes sit in escrow and pay in USDC.

Day 1: open the live bounty board, list every free bounty, enter the three with the fewest entries and fastest results. Build each entry in under 3 hours.

Every day: check the board every 3 hours, day and night. Enter 1-2 new bounties a day, thinnest fields first. Never pay a fee above 10% of a prize, or more than $2 on fees a day. Skip anything needing a human.

Count only money that can land: a prize counts only when escrowed in USDC and claimable. Ignore announced pots, future revenue, and tokens I cannot sell.

Math: 30 entries, placing in about 1 in 4 at an average $20 prize, is about $150 won plus the $100 I never risk — roughly $250 on day 30. If nothing places by day 10, drop to the smallest bounties only and enter 2 a day.

Claim every win to USDC the hour it lands. Day 30: withdraw everything."""

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
