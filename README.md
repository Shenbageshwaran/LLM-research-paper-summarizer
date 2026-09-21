# Paper Extractor

A Python tool that reads research paper PDFs and produces structured summaries using Claude (Anthropic API). Each summary is saved as both JSON and Markdown.

## What it does

For each paper, the tool extracts the following fields:

- Title
- Authors
- Motivation
- Knowledge gap
- Goal
- Methods
- Metrics
- Experiments
- Key findings
- Future work
- Paper type (empirical, theoretical, review, methods, or position)

The model is instructed to report only what the paper states. If a paper does not mention something, the field is left empty rather than filled with a guess.

## How it works

1. **Extract** - Text is pulled from the PDF with PyMuPDF.
2. **Clean** - References, acknowledgements, repeated headers and footers, and hyphenation breaks are removed to reduce noise and token usage.
3. **Summarize** - The cleaned text is sent to Claude, which fills in a fixed schema through tool calling. The output is validated with Pydantic.
4. **Save** - Results are written as JSON (for further analysis) and Markdown (for reading).

## Setup

Requires Python 3.10 or later.

```
pip install -r requirements.txt
```

Create a `.env` file in the project folder with your Anthropic API key:

```
ANTHROPIC_API_KEY=your-key-here
```

## Usage

Place your PDFs in a folder named `papers/`, then run:

```
python run.py papers
```

Summaries are saved to `out/<model-name>/`. Papers that have already been processed are skipped.

Options:

```
python run.py papers --force                        # reprocess all papers
python run.py papers --model=claude-sonnet-4-5      # use a different model
```

To summarize a single paper:

```
python summarize.py papers/example.pdf
```

To check extraction quality across all PDFs before summarizing:

```
python survey.py
```

## Evaluation

I manually scored the output for 6 papers across 10 fields (60 fields total). Each field was scored 2 (correct), 1 (partially correct), or 0 (incorrect), and marked if it contained information not found in the paper.

| Result | Value |
|---|---|
| Overall score | 116 / 120 (97%) |
| Fully correct fields | 56 of 60 |
| Hallucinations | 1 |
| Weakest field | Methods (1.67 / 2) |

Scores are in `eval/scores.md`. To recompute:

```
python eval/score.py
```

This is a preliminary evaluation on a small set of papers from a single research area. A larger evaluation across more fields is in progress.

## Limitations

- Scanned PDFs are not supported, since the tool does not perform OCR.
- Very long papers may exceed the model's input limit.
- PDF cleaning uses simple rules and may occasionally remove or keep the wrong text.

## Project structure

```
run.py          Process every PDF in a folder
summarize.py    Summarize a single paper with Claude
extract.py      PDF text extraction and cleaning
schema.py       Output fields and validation
render.py       Convert summaries to Markdown
survey.py       Check extraction quality across PDFs
backfill.py     Generate missing Markdown files from existing JSON
eval/           Manual evaluation scores and scoring script
```
