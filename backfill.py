"""Generate missing .md files from existing .json output."""

import json
from pathlib import Path

from schema import PaperSummary
from render import to_markdown

OUT = Path("out")

for json_file in sorted(OUT.glob("*.json")):
    md_file = json_file.with_suffix(".md")
    if md_file.exists():
        continue

    data = json.loads(json_file.read_text(encoding="utf-8"))
    summary = PaperSummary.model_validate(data)
    md_file.write_text(to_markdown(summary), encoding="utf-8")
    print(f"wrote {md_file.name}")