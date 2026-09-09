'''
Exercise 14: Compare Retrieved Documents

Problem:
An AI application retrieves documents using two different
retrieval methods.

Vector search returned:

vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104"
}

Keyword search returned:

keyword_results = {
    "doc_102",
    "doc_103",
    "doc_105"
}

Find TWO things:

1. Documents found by BOTH retrieval methods.
2. Documents found by EITHER retrieval method, including
   documents that appeared in only one method.

Store them in:

common_documents
all_documents

Print both variables.

Expected output:

common_documents:
{'doc_102', 'doc_103'}

all_documents:
{'doc_101', 'doc_102', 'doc_103', 'doc_104', 'doc_105'}

Use set operations. Do not use loops.
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
all_documents = vector_results.union(keyword_results)
print(common_documents)
print(all_documents)
