'''
Exercise 11: Find Unique Documents Across Search Results

Problem:
An AI application performs two searches.

First search results:

search_1 = {
    "doc_101",
    "doc_102",
    "doc_103"
}

Second search results:

search_2 = {
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}

Create a set called `all_documents` containing every unique
document ID found across both searches.

Print `all_documents`.

Expected output:
{'doc_101', 'doc_102', 'doc_103', 'doc_104', 'doc_105'}

Use `set.update()` for this exercise.
'''

# solution
search_1 = {
    "doc_101",
    "doc_102",
    "doc_103"
}

search_2 = {
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}

all_document = set()
all_document.update(search_1)
all_document.update(search_2)
print(all_document)

