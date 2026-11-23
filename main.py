import os

# One line, one sentence, at most 200 characters: the gate rejects
# anything longer, empty, or whitespace-only, so keep it short.
LINE = (
    "I bought a standing desk to get healthier, "
    "so now I sit on a taller chair and call it progress."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
