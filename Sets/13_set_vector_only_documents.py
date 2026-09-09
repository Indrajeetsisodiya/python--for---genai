'''
Exercise 13: Find Documents Only in Vector Search

Problem:
An AI application uses two retrieval methods.

Vector search found:

vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104"
}

Keyword search found:

keyword_results = {
    "doc_102",
    "doc_103",
    "doc_105"
}

Find the documents that were found by vector search
but NOT by keyword search.

Store the result in `vector_only_documents`.

Print `vector_only_documents`.

Expected output:
{'doc_101', 'doc_104'}

Hint:
Think about the set operation that finds elements
in the first set but not the second.
'''

# solution
vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104"
}

keyword_results = {
    "doc_102",
    "doc_103",
    "doc_105"
}

vector_only_documents = vector_results.difference(keyword_results)
print(vector_only_documents)

