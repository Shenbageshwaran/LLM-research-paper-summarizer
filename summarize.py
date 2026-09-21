"""Stage 3: extract a structured summary from one paper."""

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from anthropic import Anthropic

from extract import extract_text, clean, rough_tokens
from schema import PaperSummary

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# MODEL = "claude-haiku-4-5-20251001"
MODEL = os.getenv("MODEL", "claude-haiku-4-5-20251001")

SYSTEM = """You extract structured information from academic papers.

Rules:
- Report only what the paper states. Never add outside knowledge.
- If the paper does not state something, return null (or an empty list).
  Do not infer, guess, or fill gaps with what is typical for the field.
- Quote or closely paraphrase the paper's own framing rather than
  restating it in generic terms.
- A null field is a correct answer when the paper is silent."""

PROMPT = """<paper>
{paper}
</paper>

Extract a structured summary of this paper using the record_summary tool."""

TOOL = {
    "name": "record_summary",
    "description": "Record the structured summary of a research paper.",
    "input_schema": PaperSummary.model_json_schema(),
}


def summarize(pdf_path: str | Path,  model: str = MODEL) -> PaperSummary:
    text = clean(extract_text(pdf_path))

    response = client.messages.create(
        model=model,
        max_tokens=4000,
        temperature=0,
        system=SYSTEM,
        tools=[TOOL],
        tool_choice={"type": "tool", "name": "record_summary"},
        messages=[{"role": "user", "content": PROMPT.format(paper=text)}],
    )

    block = next(b for b in response.content if b.type == "tool_use")
    summary = PaperSummary.model_validate(block.input)

    u = response.usage
    print(f"  tokens in: {u.input_tokens:,}  out: {u.output_tokens:,}")
    return summary, u.input_tokens, u.output_tokens


if __name__ == "__main__":
    path = Path(sys.argv[1])
    print(f"{path.name}")

    result = summarize(path)

    out_dir = Path("out")
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / (path.stem + ".json")
    out_file.write_text(
        json.dumps(result.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"  written to {out_file}\n")
    print(json.dumps(result.model_dump(), indent=2, ensure_ascii=False))