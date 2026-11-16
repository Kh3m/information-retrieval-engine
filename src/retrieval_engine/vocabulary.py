class Vocabulary:
    def __init__(self):
        self.term_to_index = {}
        self.index_to_term = []

    def add_tokens(self, tokens: list[str]):
        for token in tokens:
            if token not in self.term_to_index:
                index = len(self.index_to_term)

                self.term_to_index[token] = index
                self.index_to_term.append(token)

    def build(self, documents: list[list[str]]) -> None:
        self.term_to_index.clear()
        self.index_to_term.clear()

        for tokens in documents:
            self.add_tokens(tokens)

    def get_index(self, term: str) -> int | None:
        return self.term_to_index.get(term)

    def get_term(self, index: int) -> str:
        return self.index_to_term[index]
