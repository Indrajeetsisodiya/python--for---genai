'''
Exercise 18: Group RAG Results by Similarity Score

Problem:
A RAG system returns search results as tuples:

(document_id, similarity_score)
Use this data:

search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68),
    ("doc_518", 0.88),
    ("doc_621", 0.79)
]

Create a function called `group_search_results`.

The function should:

1. Receive `search_results`.
2. Create two empty lists:
   - `high_score`
   - `low_score`
3. Loop through the results using tuple unpacking.
4. If the similarity score is greater than or equal to 0.85,
   add the entire tuple to `high_score`.
5. Otherwise, add the entire tuple to `low_score`.
6. Return both lists together as a tuple.

Call the function and use tuple unpacking to store the returned
lists in:

- `high_results`
- `low_results`

Print both lists.

Expected output:

High:
[('doc_101', 0.92), ('doc_309', 0.95), ('doc_518', 0.88)]

Low:
[('doc_205', 0.71), ('doc_412', 0.68), ('doc_621', 0.79)]
'''

# solution
search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68),
    ("doc_518", 0.88),
    ("doc_621", 0.79)
]
def group_search_results(search_results):
    high_score = []
    low_score = []

    for i in search_results:
        document_id,similarity_score = i
        if similarity_score >= 0.85:
            high_score.append(i)
        else:
            low_score.append(i)
    return high_score, low_score

high_results,low_results = group_search_results(search_results)
print(high_results)
print(low_results)