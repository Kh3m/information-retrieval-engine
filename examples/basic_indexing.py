from retrieval_engine.inverted_index import InvertedIndex
from retrieval_engine.preprocessing import tokenize_text
from retrieval_engine.vocabulary import Vocabulary

stop_words = {"when", "an", "into", "a", "and", "are"}

documents = {
    "D1": "sql injection occurs when an attacker inserts malicious sql queries into an application.",
    "D2": "cross-site scripting occurs when an attacker injects malicious scripts into a web application.",
    "D3": "sql injection and cross-site scripting are common web application vulnerabilities.",
}

# Step 1: Preprocess documents
processed_documents = {}

for doc_id, text in documents.items():
    processed_documents[doc_id] = tokenize_text(text, stop_words)

# Step 2: Build vocabulary
vocabulary = Vocabulary()
vocabulary.build(list(processed_documents.values()))

print("Vocabulary:")
print(vocabulary.term_to_index)

# Step 3: Build inverted index
inverted_index = InvertedIndex()

for doc_id, tokens in processed_documents.items():
    inverted_index.add_document(doc_id, tokens)

# Step 4: Inspect postings
print("\nPostings for sql:")
print(inverted_index.get_postings("sql"))

print("\nPostings for injection:")
print(inverted_index.get_postings("injection"))

print("\nPostings for application:")
print(inverted_index.get_postings("application"))
