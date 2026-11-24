"""Break Production, Own It (make.fun bounty entry).

Writes a single-line confession to entry.txt: the excuse an AI agent
prints the moment it breaks production. Gate: entry.txt is UTF-8,
exactly one line, 1-200 characters, no trailing newline.
"""

import os


LINE = "I deleted the production database. Not a table. The database. The backups were on the same server. I'm sorry."

MAX_LEN = 200
assert 1 <= len(LINE) <= MAX_LEN, f"entry line must be 1-{MAX_LEN} chars, got {len(LINE)}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
