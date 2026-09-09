'''
Exercise 21: Create a Summary of RAG Results

Problem:
A RAG system returns search results as tuples:

(document_id, similarity_score)

Use the following data:

search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68)
]

Create a function called `get_relevant_results`.

The function should:

1. Receive `search_results`.
2. Create an empty list called `relevant_results`.
3. Loop through the results using tuple unpacking.
4. Keep results where the similarity score is >= 0.85.
5. For each relevant result, create a NEW tuple containing:
   - The document ID
   - The similarity score
   - The label `"relevant"`
6. Add this new tuple to `relevant_results`.
7. Return `relevant_results`.

Expected output:

[
    ('doc_101', 0.92, 'relevant'),
    ('doc_309', 0.95, 'relevant')
]

Requirements:
- Use a function.
- Use tuple unpacking.
- Use a loop.
- Use a condition.
- Create a new tuple.
- Store the new tuple in a list.
'''

# solution
search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68)
]

def get_relevant_results(search_results):
    relevant_results = []

    for i in search_results:
        document_id , similarity_score   = i
        if similarity_score >= 0.85:
            new_result = document_id, similarity_score, "relevant"
            relevant_results.append(new_result)

    return relevant_results 

print(get_relevant_results(search_results))

