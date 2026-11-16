from retrieval_engine.inverted_index import InvertedIndex

inverted_index = InvertedIndex()


def test_add_document():
    inverted_index.add_document("doc1", ["love", "python", "programming", "love"])
    assert len(inverted_index.get_index()) == 3


def test_postings_for_non_existing_token():
    assert {} == inverted_index.get_postings("non_existing_token")


def test_postings_for_existing_token():
    assert {"doc1": 2} == inverted_index.get_postings("love")
