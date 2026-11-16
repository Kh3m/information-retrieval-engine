from copy import deepcopy


class InvertedIndex:
    def __init__(self):
        self._index = {}

    def add_document(self, doc_id: str, tokens: list[str]) -> None:
        for token in tokens:
            token_value = self._index.get(token, {})
            token_value[doc_id] = token_value.get(doc_id, 0) + 1
            self._index[token] = token_value

    def get_postings(self, token: str) -> dict[str, int]:
        return self._index.get(token, {})

    def get_index(self) -> dict[str, dict[str, int]]:
        return deepcopy(self._index)
