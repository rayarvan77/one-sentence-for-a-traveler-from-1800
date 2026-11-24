"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800.

The vocabulary rule: every word in the sentence must predate 1800, so the
traveler can understand it with the knowledge he already carries. A word
is allowed only if a person living in 1800 could know what it means:
"library", "book", "letter", "breath" are fine, because libraries, books,
letters and breaths all existed then. Any word coined after 1800 — or tied
to an invention that came later — is rejected, because the traveler would
have no referent for it. Examples of rejected words: "internet" (the
network itself did not exist), "computer" (coined in the 20th century for
a calculating machine), and "telegraph" (the electric telegraph arrived
in the 1830s-1840s, decades after the traveler left). The same rule bars
"email", "website", "software", "robot", "pixel" and every other entry in
the denylist below; the sentence is checked word by word against it.

The form rules are just as strict: exactly one sentence, so the whole
explanation must fit in a single breath of thought, and at most 200
characters, so it stays short enough to be spoken aloud in one go. The
sentence must end with exactly one period and contain no other
sentence-ending marks, so there is no room for a second sentence to hide.

Deterministic, Python 3.13 standard library only, no network access.
Writes the sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it.
"""

import os
import sys

# The sentence: one image a traveler from 1800 could hold in his head.
# A great library holding every book ever printed stands for all the
# knowledge the internet holds; a letter sent and answered in the same
# breath stands for instant writing between any two people on earth.
SENTENCE = (
    "Picture a great library holding every book ever printed, where any "
    "man may send a letter to any other man on earth and read his reply "
    "in the same breath."
)

# Words coined after 1800 (or tied to inventions after the traveler's
# time) that must never appear in the sentence. Checked case-insensitively
# as whole words, so a word like "letter" is never caught by "telegraph".
DENYLIST = {
    "internet", "computer", "online", "screen", "digital", "network",
    "telegraph", "telephone", "website", "email", "software", "data",
    "video", "audio", "wireless", "electric", "electronic", "keyboard",
    "mouse", "server", "browser", "download", "upload", "stream",
    "smartphone", "phone", "radio", "television", "robot", "ai",
    "cyber", "virtual", "pixel", "code", "program", "app", "chat",
    "message", "text", "device", "machine", "engine", "signal",
    "photograph", "satellite", "airplane", "automobile", "plastic",
    "rocket", "laser", "microwave",
}

MAX_CHARS = 200


def validate(sentence: str) -> None:
    """Fail loudly if the sentence breaks any rule of the brief."""
    text = sentence.strip()
    if not text:
        raise ValueError("sentence is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    # Exactly one sentence: one period, at the very end, no other
    # sentence-ending marks. The sentence must end with exactly one
    # period: a doubled period ("..") or a period anywhere but the end
    # would mean two sentences, or a sentence cut short.
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("sentence must be exactly one sentence ending in '.'")
    if text.endswith(".."):
        raise ValueError("sentence must end with exactly one period")
    if any(mark in text for mark in ("!", "?", ";", ":", "\n")):
        raise ValueError("sentence must be a single plain sentence")
    words = text.lower().replace(".", "").replace(",", "").split()
    banned = sorted(set(words) & DENYLIST)
    if banned:
        raise ValueError(f"post-1800 words in sentence: {', '.join(banned)}")


def main() -> int:
    validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(SENTENCE)
    print(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
