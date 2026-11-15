from retrieval_engine.processing import tokenize_text


def test_tokenize_lowercase():
    assert tokenize_text("SQL INJECTION") == ["sql", "injection"]


def test_tokenize_punctuation():
    assert tokenize_text("sql, injection!") == ["sql", "injection"]


def test_tokenize_hyphenated_words():
    assert tokenize_text("cross-site scripting") == [
        "cross",
        "site",
        "scripting",
    ]


def test_tokenize_stop_words():
    stop_words = {"when", "an", "into"}

    result = tokenize_text(
        "sql injection occurs when an attacker inserts data into an application",
        stop_words,
    )

    assert result == [
        "sql",
        "injection",
        "occurs",
        "attacker",
        "inserts",
        "data",
        "application",
    ]


def test_tokenize_repeated_words():
    assert tokenize_text("sql sql injection") == [
        "sql",
        "sql",
        "injection",
    ]
