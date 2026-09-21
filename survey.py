"""Sanity-check extraction quality across every PDF in papers/."""

from pathlib import Path

from extract import extract_text, clean, rough_tokens

PAPERS = Path("papers")

print(f"{'file':45s} {'raw':>9s} {'clean':>9s} {'tokens':>8s} {'cut':>6s}")
print("-" * 82)

total_tokens = 0
problems = []

for pdf in sorted(PAPERS.glob("*.pdf")):
    try:
        raw = extract_text(pdf)
        cleaned = clean(raw)
    except Exception as e:
        problems.append((pdf.name, f"failed to open: {e}"))
        continue

    tokens = rough_tokens(cleaned)
    total_tokens += tokens
    cut = 100 * (1 - len(cleaned) / len(raw)) if raw else 0

    name = pdf.name if len(pdf.name) <= 44 else pdf.name[:41] + "..."
    print(f"{name:45s} {len(raw):9,} {len(cleaned):9,} {tokens:8,} {cut:5.0f}%")

    if len(raw) < 1000:
        problems.append((pdf.name, "almost no text — likely a scanned PDF"))
    elif cut > 60:
        problems.append((pdf.name, f"cut {cut:.0f}% — marker probably fired too early"))
    elif tokens > 100_000:
        problems.append((pdf.name, f"{tokens:,} tokens — unusually large"))

print("-" * 82)
print(f"{'TOTAL':45s} {'':9s} {'':9s} {total_tokens:8,}")

if problems:
    print("\nNeeds a look:")
    for name, issue in problems:
        print(f"  {name}: {issue}")
else:
    print("\nNo obvious problems.")