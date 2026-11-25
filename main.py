"""Snooze Button Roast entry: one line roasting a 6 AM Saturday alarm.

Writes the roast to the path in OUTPUT_PATH (default /output/entry.txt),
exactly one line, no trailing newline.
"""

import os

ROAST = (
    "My alarm at 6 AM Saturday is a GPS that lost signal in 2019 "
    "and still insists I turn left into Monday."
)


def resolve_output_path() -> str:
    """Return the entry output path, creating its parent directory."""
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    return output_path


def main() -> None:
    output_path = resolve_output_path()
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
