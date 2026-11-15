# Information Retrieval Engine

A reusable information retrieval engine written in Python. It is designed to be the
retrieval layer for other systems, such as a property insights platform or the
retrieval step of a RAG (retrieval-augmented generation) pipeline. Given a collection
of documents and a query, it returns the most relevant documents.

Text processing, vocabulary, and indexing are separate modules, so a consuming system
can use only the parts it needs.

## Status

- [x] Text preprocessing (tokenization, lowercasing, stop-word removal)
- [ ] Vocabulary
- [ ] Index
- [ ] Querying and ranking
- [ ] Installable package / public API for other systems

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Setup

```sh
uv sync
```

This creates `.venv/` and installs the dev dependencies (pytest) from `uv.lock`.

## Project layout

```
src/retrieval_engine/
    processing.py   # text preprocessing (tokenize_text)
    vocabulary/     # (planned)
    index/          # (planned)
tests/
    test_preprocessing.py
```

## Usage

The package isn't installed into the venv yet (there is no `[build-system]`), so put
`src/` on the path when running scripts outside pytest, e.g. `PYTHONPATH=src uv run python`.

```python
from retrieval_engine.processing import tokenize_text

tokenize_text("SQL Injection, cross-site scripting!")
# ['sql', 'injection', 'cross', 'site', 'scripting']

tokenize_text("sql injection occurs when an attacker", stop_words={"when", "an"})
# ['sql', 'injection', 'occurs', 'attacker']
```

`tokenize_text` lowercases the text, splits on anything that isn't a letter or digit
(so punctuation and hyphens act as separators), and optionally removes stop words.
Repeated tokens are kept.

## Running tests

```sh
uv run pytest
```

`uv run` syncs the virtual environment with `uv.lock` and runs pytest inside it.
Pytest is configured in `pyproject.toml` to add `src/` to the import path and to
collect tests from `tests/`.

Useful variations:

```sh
uv run pytest -v                          # one line per test
uv run pytest -k punctuation              # only tests whose name matches
uv run pytest -x                          # stop at the first failure
```
