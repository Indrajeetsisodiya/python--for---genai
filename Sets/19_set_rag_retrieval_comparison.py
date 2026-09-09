'''
Exercise 19: RAG Retrieval Comparison

Problem:
An AI application uses two retrieval systems.

Vector search returned:

vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}

Keyword search returned:

keyword_results = {
    "doc_103",
    "doc_104",
    "doc_105",
    "doc_106"
}

Find TWO things:

1. Documents found by BOTH retrieval systems.
2. Documents found ONLY by vector search.

Store them in:

common_documents
vector_only_documents

Print both variables.

Expected output:

common_documents:
{'doc_103', 'doc_104', 'doc_105'}

vector_only_documents:
{'doc_101', 'doc_102'}

Use set operations. Do not use loops.
'''

# solution
vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}

keyword_results = {
    "doc_103",
    "doc_104",
    "doc_105",
    "doc_106"
}

common_documents = vector_results.intersection(keyword_results)
vector_only_documents = vector_results.difference(keyword_results)
print(common_documents)
print(vector_only_documents)
