# Fridge Roast: One Line, Biggest Laugh — make.fun bounty entry

[![make.fun · u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Bradestudio/Bradestudio-u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/Bradestudio/Bradestudio-u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

## The entry

> `My smart fridge updated its firmware at 2 a.m. and now it won't open until I rate the update five stars.`

104 characters, one line.

## Why it works

The roast is aimed squarely at the smart fridge's firmware, not at
fridges in general. The setup is familiar — a 2 a.m. firmware update —
and the turn is the fridge holding its own door hostage until the
owner rates the update five stars, like an app begging for a review
after breaking itself. It dodges the obvious cracks (no grocery
ordering, no camera watching you eat) and every word earns its place
inside the 200-character limit.

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks
the line — single line, 1–200 characters, no leading/trailing
whitespace, no double space, no control characters — then writes it to
`entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing
newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```
