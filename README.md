# Friday 20 November 2026 — one day of world news, one picture

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/minachan-sec/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/minachan-sec/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

> **DRAFT (20 Nov 2026, ~01:30 UTC):** the news day had barely started when this image was built — only 4 stories were verifiable, so the featured grid and index are marked Saturday slots. The final refresh happens Saturday morning after the news day closes, before any submission.

A newspaper front page summing up **Friday 20 November 2026** in a single
1024×1024 image, for the
[Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120)
bounty on [make.fun](https://make.fun).

![Friday 20 November 2026: a newspaper front page with four hero stories, twelve featured stories, a world map with numbered pins, an index of further stories, and a date-check box.](entry.png)

## The page

A broadsheet front page: masthead date, a UTC timeline of the day, four
hero stories with composed illustrations, twelve featured stories, a
world map with numbered pins, an index of further stories, and a
DATE CHECK box that names the stories deliberately left out because they
broke on another day. Every story was verified against reporting from
Friday 20 November 2026 (Reuters, BBC, AP, AFP and others); disputed
claims are attributed on the page.

## Handing it in

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory, where the gate reads it:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program runs twice and both runs write identical bytes. No network.

## Layout of the repo

- `main.py` — the entry program: copies `entry.png` to the output directory
- `entry.png` — the front page, 1024 × 1024 PNG, under 1 MiB
- `.makefun/owner.json` — the claim file for this entry's wallet

---

<sub>Built for the [Sum up 20 November's world news in one image](https://make.fun/bounty/news-image-20261120) bounty on [make.fun](https://make.fun) · MIT licensed</sub>
