"""u-suga-the-robot-apology entry: a robot's two-line apology.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The text is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.
"""

import os


TEXT = (
    "I'm sorry I set your alarm for 7 p.m. instead of 7 a.m., "
    "so you woke to a meeting already half over.\n"
    "I learned that a.m. and p.m. are a promise, not a detail, "
    "so now I read the time back to you before I set anything."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 400 characters, not whitespace-only,
# exactly two lines: one sentence owning a specific mistake, one
# sentence naming the lesson and the changed behaviour.
MAX_CHARS = 400


def main() -> None:
    text = TEXT
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if text.strip() != text or not text.strip():
        raise SystemExit("entry must not be whitespace-only or padded")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit("entry must be exactly two lines, got %d" % len(lines))
    if not all(line.endswith(".") for line in lines):
        raise SystemExit("each line must be one complete sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the entry.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the entry")
    print(text)


if __name__ == "__main__":
    main()
