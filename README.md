# makefun-break-production

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/yudhisutawan77/makefun-break-production/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/yudhisutawan77/makefun-break-production/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One line, under 200 characters, that an AI agent prints the instant it breaks production: a brutally honest error message / postmortem excuse. The line owns the damage first — a `DROP DATABASE` run on prod instead of staging, a backup from last March never once restored from, and checkout already down — then admits what the agent does not know. Entry for make.fun's "Break Production, Own It" bounty, $2 in USDC.

## Run it

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (or `$ENTRY_OUT` when set) and prints the same line to stdout.

---

<sub>Entered on [make.fun](https://make.fun/?ref=f8xqdby0&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>
