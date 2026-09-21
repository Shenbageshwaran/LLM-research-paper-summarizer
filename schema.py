"""Schema for extracted paper summaries."""

from typing import Optional
from pydantic import BaseModel, Field
from pydantic import field_validator
import re

def _to_list(v):
    """Recover a list when the model returns markup or plain text."""
    if isinstance(v, list):
        return v
    if not isinstance(v, str):
        return v
    items = re.findall(r"<item>(.*?)</item>", v, flags=re.DOTALL)
    if not items:
        items = [line.lstrip("-•* ").strip()
                for line in v.split("\n") if line.strip()]
    return [i.strip() for i in items if i.strip()]

class PaperSummary(BaseModel):
    title: str = Field(description="Full title of the paper")

    authors: list[str] = Field(
    default_factory=list,
    description=(
        "Author names in order, one per item. Names may be split across "
        "lines and interleaved with superscript affiliation markers "
        "(a, b, c, *) and stray commas — reassemble each full name and "
        "strip all markers. Return e.g. 'Jane Smith', not 'Jane Smith a,b*'."
    ),
    )

    motivation: str = Field(
        description="Why this problem matters, as the paper argues it"
    )

    knowledge_gap: Optional[str] = Field(
        default=None,
        description=(
            "The specific limitation in prior work this paper addresses. "
            "Null if the paper does not state one explicitly."
        ),
    )

    goal: str = Field(
        description="What the authors set out to do; the stated objective"
    )

    methods: list[str] = Field(
        default_factory=list,
        description="Techniques, algorithms, or approaches used",
    )

    metrics: list[str] = Field(
        default_factory=list,
        description=(
            "Quantitative measures used to evaluate results "
            "(accuracy, F1, runtime, etc.). Empty if none reported."
        ),
    )

    experiments: Optional[str] = Field(
        default=None,
        description=(
            "Datasets, case studies, or experimental setup. "
            "Null for purely theoretical or review papers."
        ),
    )

    key_findings: list[str] = Field(
        default_factory=list,
        description="Main results or conclusions, one per item",
    )

    future_work: list[str] = Field(
        default_factory=list,
        description="Limitations or future directions the authors name",
    )

    paper_type: str = Field(
        description="One of: empirical, theoretical, review, methods, position"
    )

    @field_validator("authors", "methods", "metrics",
                     "key_findings", "future_work", mode="before")

    @classmethod

    def coerce_list(cls, v):
        return _to_list(v)




