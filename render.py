"""Turn a PaperSummary into readable Markdown."""

from schema import PaperSummary


def _bullets(items: list[str]) -> str:
    if not items:
        return "_none stated_\n"
    return "\n".join(f"- {i}" for i in items) + "\n"


def _field(value: str | None) -> str:
    return value if value else "_not stated in the paper_"


def to_markdown(s: PaperSummary) -> str:
    parts = [
        f"# {s.title}\n",
        f"**Authors:** {', '.join(s.authors) if s.authors else 'unknown'}  ",
        f"**Type:** {s.paper_type}\n",
        "## Motivation\n", _field(s.motivation) + "\n",
        "## Knowledge gap\n", _field(s.knowledge_gap) + "\n",
        "## Goal\n", _field(s.goal) + "\n",
        "## Methods\n", _bullets(s.methods),
        "## Metrics\n", _bullets(s.metrics),
        "## Experiments\n", _field(s.experiments) + "\n",
        "## Key findings\n", _bullets(s.key_findings),
        "## Future work\n", _bullets(s.future_work),
    ]
    return "\n".join(parts)