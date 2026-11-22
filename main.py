"""Hand the tasting picture to the grader.

Copies the hero ingredient shot beside this file into /output so the
judge can taste it with its eyes. Standard library only.
"""
import shutil
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent
    picture = root / "entry.png"
    if not picture.is_file():
        raise SystemExit(f"entry picture missing: {picture}")
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(picture, out / "entry.png")
    print("picture delivered to /output/entry.png")

if __name__ == "__main__":
    main()
