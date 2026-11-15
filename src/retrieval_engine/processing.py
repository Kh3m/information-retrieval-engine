import re


def tokenize_text(text: str, stop_words: set[str] | None = None) -> list[str]:
    """
    Tokenizes the input text into a list of tokens.

    Args:
        text (str): The input text to be tokenized.
        stop_words (set[str], optional): A set of stop words to be removed from the tokens.

    Returns:
        list: A list of tokens extracted from the input text.
    """

    # Simple whitespace tokenization
    tokens = re.findall(r"[a-z0-9]+", text.lower())

    if stop_words:
        tokens = [token for token in tokens if token not in stop_words]
    return tokens
