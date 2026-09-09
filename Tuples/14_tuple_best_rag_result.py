'''
Exercise 14: Find the Best RAG Result

Problem:
A RAG system returns search results as tuples:

(document_id, similarity_score)

Use the following data:

search_results = [
    ("doc_101", 0.82),
    ("doc_205", 0.91),
    ("doc_309", 0.87),
    ("doc_412", 0.95),
    ("doc_518", 0.89)
]

Find the document with the highest similarity score.

Store:

- The document ID in `best_document`
- The score in `best_score`

Finally, print both values.

Expected output:
doc_412
0.95

Requirements:
- Use a `for` loop.
- Use tuple unpacking.
- Do not use `max()`.
'''

# solution
search_results = [
    ("doc_101", 0.82),
    ("doc_205", 0.91),
    ("doc_309", 0.87),
    ("doc_412", 0.95),
    ("doc_518", 0.89)
]
best_score = 0
best_document = ""
for document_id, similarity_score in search_results:
    if similarity_score > best_score:
        best_score = similarity_score
        best_document = document_id

print(best_document)
print(best_score)
