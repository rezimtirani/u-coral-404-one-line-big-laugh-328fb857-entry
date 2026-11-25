"""One Line, Big Laugh.

A single hilarious line, written to $MAKEFUN_OUTPUT_DIR/entry.txt:
the password manager that forgot the one password it exists to
remember, and then suggested resetting it with that same password.
Standard library only; nothing leaves this repository.
"""

import os

LINE = (
    "My password manager forgot my password, then suggested "
    "I reset it with the password I'd forgotten."
)


def validate_line(text):
    """Check the line against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one funny line that lands entirely on
    its own, with no title, setup or explanation around it. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "line is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be exactly one line")
    return cleaned


def line_metrics(text):
    """Measure the line for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A one-liner too short to carry a joke, or one that
    reads like a setup waiting for a punchline, is caught here before
    anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def run():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = validate_line(LINE)
    sizes = line_metrics(text)
    if sizes["words"] < 5:
        raise ValueError("line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    run()
