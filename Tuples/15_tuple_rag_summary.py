'''
Exercise 15: Build a RAG Result Summary

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

Create a function called `get_best_result`.

The function should:

1. Receive `search_results` as an argument.
2. Find the document with the highest similarity score.
3. Return the document ID and score together as a tuple.

Then call the function and use tuple unpacking to store the returned values in:

- `best_document`
- `best_score`

Finally, print both values.

Expected output:
doc_412
0.95

Requirements:
- Use a function.
- Use a for loop.
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

def get_best_results(search_results):
    highest_score = 0
    document = ""
    for document_id , similarity_score in search_results:
        if similarity_score > highest_score:
            highest_score = similarity_score
            document = document_id

    return document , highest_score

best_document , best_score = get_best_results(search_results)
print(best_document)
print(best_score)

    