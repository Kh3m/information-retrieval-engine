# Information Retrieval Engine

A reusable information retrieval engine written in Python. It is designed to be the
retrieval layer for other systems, such as a property insights platform or the
retrieval step of a RAG (retrieval-augmented generation) pipeline. Given a collection
of documents and a query, it returns the most relevant documents.

Text processing, vocabulary, and indexing are separate modules, so a consuming system
can use only the parts it needs.

## Status

- [x] Text preprocessing (tokenization, lowercasing, stop-word removal)
- [x] Vocabulary (term ↔ index mapping)
- [x] Inverted index (term → document → frequency)
- [ ] Querying and ranking
- [x] Installable package (editable install via `uv sync`)
- [ ] Public API for other systems

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

## Setup

```sh
uv sync
```

This creates `.venv/`, installs the dev dependencies (pytest) from `uv.lock`, and
installs `retrieval_engine` itself in editable mode. Because `pyproject.toml` defines a
`[build-system]` (hatchling), `retrieval_engine` can be imported from anywhere in the
project, and changes to the source files take effect without reinstalling.

## Project layout

```
src/retrieval_engine/
    preprocessing.py    # tokenize_text
    vocabulary.py       # Vocabulary
    inverted_index.py   # InvertedIndex
examples/
    basic_processing.py
    basic_indexing.py
tests/
    test_preprocessing.py
    test_vocabulary.py
    test_inverted_index.py
```

## Usage

### Preprocessing

```python
from retrieval_engine.preprocessing import tokenize_text

tokenize_text("SQL Injection, cross-site scripting!")
# ['sql', 'injection', 'cross', 'site', 'scripting']

tokenize_text("sql injection occurs when an attacker", stop_words={"when", "an"})
# ['sql', 'injection', 'occurs', 'attacker']
```

`tokenize_text` lowercases the text, splits on anything that isn't a letter or digit
(so punctuation and hyphens act as separators), and optionally removes stop words.
Repeated tokens are kept.

### Vocabulary

```python
from retrieval_engine.vocabulary import Vocabulary

vocabulary = Vocabulary()
vocabulary.build([["sql", "injection"], ["sql", "scripting"]])

vocabulary.get_index("scripting")  # 2
vocabulary.get_term(0)             # 'sql'
vocabulary.get_index("missing")    # None
```

`Vocabulary` assigns each unique term an integer index in the order it is first seen.
`build` resets the vocabulary before adding documents; `add_tokens` adds to it.

### Inverted index

```python
from retrieval_engine.inverted_index import InvertedIndex

index = InvertedIndex()
index.add_document("D1", ["sql", "injection", "sql"])
index.add_document("D2", ["sql", "scripting"])

index.get_postings("sql")      # {'D1': 2, 'D2': 1}
index.get_postings("missing")  # {}
```

`InvertedIndex` maps each term to the documents it appears in and how many times.
`get_index` returns a copy of the whole index, so callers can't modify it by accident.

## Examples

```sh
uv run python examples/basic_processing.py
uv run python examples/basic_indexing.py
```

`basic_indexing.py` runs the full pipeline: preprocess documents, build a vocabulary,
build an inverted index, and print postings for a few terms.

## Running tests

```sh
uv run pytest
```

`uv run` syncs the virtual environment with `uv.lock` and runs pytest inside it.
Tests are collected from `tests/` (configured in `pyproject.toml`).

Useful variations:

```sh
uv run pytest -v                          # one line per test
uv run pytest -k punctuation              # only tests whose name matches
uv run pytest -x                          # stop at the first failure
```
