"""Stage 4: process every PDF in a folder."""

import json
import sys
import time
from pathlib import Path

from extract import extract_text, clean, rough_tokens
from schema import PaperSummary
from summarize import summarize, MODEL
from render import to_markdown
import re

OUT = Path("out")


def process_folder(folder: Path, force: bool = False, model: str = MODEL) -> None:
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", model.split("-2025")[0])
    out = Path("out") / safe
    out.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(folder.glob("*.pdf"))
    if not pdfs:
        print(f"no PDFs found in {folder}")
        return

    done = skipped = failed = 0
    start = time.time()

    for i, pdf in enumerate(pdfs, 1):
        json_path = out / f"{pdf.stem}.json"
        md_path = out / f"{pdf.stem}.md"
        print(f"[{i}/{len(pdfs)}] {pdf.name}")

        if json_path.exists() and md_path.exists() and not force:
            print("  cached, skipping")
            skipped += 1
            continue

        try:
            text = clean(extract_text(pdf))
            if rough_tokens(text) < 500:
                raise ValueError("too little text — scanned or empty PDF?")

            summary, tin, tout = summarize(pdf, model=model)

            json_path.write_text(
                json.dumps(summary.model_dump(), indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            md_path.write_text(to_markdown(summary), encoding="utf-8")
            done += 1

        except Exception as e:
            print(f"  FAILED: {type(e).__name__}: {e}")
            failed += 1
            continue

    elapsed = time.time() - start
    print(f"\n{done} processed, {skipped} cached, {failed} failed "
          f"in {elapsed:.0f}s")


if __name__ == "__main__":
    args = sys.argv[1:]
    force = "--force" in args
    model = next((a.split("=", 1)[1] for a in args if a.startswith("--model=")), MODEL)
    paths = [a for a in args if not a.startswith("--")]
    folder = Path(paths[0]) if paths else Path("papers")
    process_folder(folder, force=force, model=model)