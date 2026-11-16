from retrieval_engine.vocabulary import Vocabulary


def test_build_vocabulary():
    documents = [
        [
            "love",
            "me",
        ],
        ["hate", "bad", "me"],
    ]

    vocabulary = Vocabulary()
    vocabulary.build(documents)

    expected_term_to_index = {"love": 0, "me": 1, "hate": 2, "bad": 3}

    assert vocabulary.term_to_index == expected_term_to_index


def test_add_tokens():
    vocabulary = Vocabulary()
    tokens = ["love", "me", "hate", "bad", "me"]
    vocabulary.add_tokens(tokens)

    expected_term_to_index = {"love": 0, "me": 1, "hate": 2, "bad": 3}

    assert vocabulary.term_to_index == expected_term_to_index


def test_get_index_and_term():
    documents = [
        [
            "love",
            "me",
        ],
        ["hate", "bad", "me"],
    ]

    vocabulary = Vocabulary()
    vocabulary.build(documents)

    assert vocabulary.get_index("love") == 0
    assert vocabulary.get_index("me") == 1
    assert vocabulary.get_index("hate") == 2
    assert vocabulary.get_index("bad") == 3
    assert vocabulary.get_index("nonexistent") is None

    assert vocabulary.get_term(0) == "love"
    assert vocabulary.get_term(1) == "me"
    assert vocabulary.get_term(2) == "hate"
    assert vocabulary.get_term(3) == "bad"
