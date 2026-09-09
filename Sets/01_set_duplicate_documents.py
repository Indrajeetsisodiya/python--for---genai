'''
Exercise 1: Remove Duplicate Document IDs

Problem:
A RAG system has retrieved these document IDs:

document_ids = [
    "doc_101",
    "doc_205",
    "doc_101",
    "doc_309",
    "doc_205",
    "doc_412",
    "doc_309"
]

Create a set called `unique_documents` from `document_ids`.

Then print `unique_documents`.

The goal is to remove duplicate document IDs automatically.

Expected output:
The set should contain:

doc_101
doc_205
doc_309
doc_412

The order does not matter because sets are unordered.

'''

# solution
document_ids = [
    "doc_101",
    "doc_205",
    "doc_101",
    "doc_309",
    "doc_205",
    "doc_412",
    "doc_309"
]

unique_documents = set(document_ids)

print(unique_documents)

    