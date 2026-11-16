from retrieval_engine.preprocessing import tokenize_text

text = "SQL injection occurs when an attacker inserts malicious SQL queries into an application."

stop_words = {"when", "an", "into", "a", "and", "are"}

tokens = tokenize_text(text, stop_words)

print("Original text:", text)
print("Processed tokens:", tokens)
print("Total tokens:", len(tokens))
print("Unique terms:", len(set(tokens)))
