"""Copy the hero-ingredient picture to /output/entry.png for judging."""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit(f"missing entry image: {src}")
    os.makedirs("/output", exist_ok=True)
    shutil.copy(src, "/output/entry.png")


if __name__ == "__main__":
    main()
