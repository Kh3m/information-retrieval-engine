from src.retrieval_engine.processing import tokenize_text

stop_words = {"when", "an", "into", "a", "and", "are"}

documents = [
    "sql injection occurs when an attacker inserts malicious sql queries into an application.",
    "cross-site scripting occurs when an attacker injects malicious scripts into a web application.",
    "sql injection and cross-site scripting are common web application vulnerabilities.",
]


for i, doc in enumerate(documents, 1):
    tokens = tokenize_text(doc, stop_words)
    print(f"D{i}: {tokens}")
    print(f"Token count: {len(tokens)}\n")
