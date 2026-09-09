'''
Exercise 12: Find Common Documents

Problem:
An AI application has two search systems.

The first system found these documents:

vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104"
}

The second system found these documents:

keyword_results = {
    "doc_102",
    "doc_103",
    "doc_105"
}

Find the documents that were found by BOTH search systems.

Store the result in `common_documents`.

Print `common_documents`.

Expected output:
{'doc_102', 'doc_103'}

Hint:
Think about the set operation that finds common elements.
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

common_documents = vector_results.intersection(keyword_results)
print(common_documents)
