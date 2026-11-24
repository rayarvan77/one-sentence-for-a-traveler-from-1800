# One Sentence for a Traveler from 1800

[![make.fun](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rayarvan77/one-sentence-for-a-traveler-from-1800/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rayarvan77/one-sentence-for-a-traveler-from-1800/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the [make.fun](https://make.fun) bounty
[One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb):
write a single sentence, at most 200 characters, that explains the modern
internet to a time traveler who has just stepped out of the year 1800.

## The sentence

> Picture a great library holding every book ever printed, where any man may
> send a letter to any other man on earth and read his reply in the same breath.

153 characters, one sentence, one period at the end.

## Why it meets the brief

- **It explains the internet.** Two things the internet is, in one picture:
  all the knowledge ever written down, and instant writing between any two
  people on earth. A traveler from 1800 knows both halves already — a
  library and a letter — so the sentence only joins them.
- **No words coined after the traveler's time.** Every word is one a person
  from 1800 could know: library, book, printed, letter, reply, breath.
  There is no "internet", "computer", "online", "screen", "digital",
  "network" — and not even "telegraph", which would already be cheating.
  `main.py` enforces this with a denylist check before it writes anything.
- **One image, no list of features.** The sentence does not catalogue what
  the internet does; it gives a single picture — a library where letters
  fly — and lets the traveler hold it.
- **True when taken literally.** The internet does hold, in effect, every
  book ever printed, and a message sent across the world does come back in
  about the time of a breath.
- **Memorable.** "Read his reply in the same breath" is the phrase that
  stays with you a week later: a letter that answers before you finish
  breathing.

## How to run it

```sh
python3 main.py
```

`main.py` validates the sentence (exactly one sentence, at most 200
characters, no post-1800 words from its denylist), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and prints it.
Python 3.13 standard library only, no network access, fully deterministic:
the same sentence is written on every run.
