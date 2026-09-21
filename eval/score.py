"""Summarize eval/scores.md into per-field and per-paper averages."""

import re
from collections import defaultdict
from pathlib import Path

rows = []
# for line in Path("eval/scores.md").read_text(encoding="utf-8").splitlines():
SCORES = Path(__file__).parent / "scores.md"
for line in SCORES.read_text(encoding="utf-8").splitlines():
# for line in Path("scores.md").read_text(encoding="utf-8").splitlines():
    if not line.strip().startswith("|") or "---" in line:
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 4 or cells[0].lower() == "paper":
        continue
    paper, field, score, hall = cells[0], cells[1], cells[2], cells[3]
    m = re.search(r"\d", score)
    if not m:
        continue
    rows.append((paper, field, int(m.group()), "H" in hall.upper()))

by_field = defaultdict(list)
by_paper = defaultdict(list)
for paper, field, score, h in rows:
    by_field[field].append(score)
    by_paper[paper].append(score)

total = sum(s for _, _, s, _ in rows)
halls = sum(1 for *_, h in rows if h)

print(f"overall: {total}/{len(rows)*2} = {100*total/(len(rows)*2):.0f}%")
print(f"hallucinations: {halls}\n")

print("by field:")
for field, scores in sorted(by_field.items(), key=lambda kv: sum(kv[1])/len(kv[1])):
    avg = sum(scores) / len(scores)
    print(f"  {field:16s} {avg:.2f}  {'█' * round(avg * 10)}")

print("\nby paper:")
for paper, scores in sorted(by_paper.items(), key=lambda kv: sum(kv[1])/len(kv[1])):
    avg = sum(scores) / len(scores)
    name = paper if len(paper) <= 40 else paper[:37] + "..."
    print(f"  {name:42s} {avg:.2f}")