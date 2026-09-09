'''
Exercise 10: Filter RAG Search Results with a Function

Problem:
A RAG system returns search results as tuples.

Each tuple contains:

(document_id, similarity_score)

Create a function called `get_relevant_documents` that receives
`search_results`.

The function should:

1. Loop through the search results.
2. Unpack each tuple into `document_id` and `score`.
3. Keep only documents whose score is greater than or equal to 0.85.
4. Store the document IDs of relevant documents in a list.
5. Return that list.

Use this data:

search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68),
    ("doc_518", 0.88)
]

Call the function and print the returned list.

Expected output:
['doc_101', 'doc_309', 'doc_518']
'''

# solution
search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.71),
    ("doc_309", 0.95),
    ("doc_412", 0.68),
    ("doc_518", 0.88)
]

my_list = []

def get_relevant_documents(search_results):
    for document_id , score in search_results:
        if score >= 0.85:
            my_list.append(document_id)
    return my_list

print(get_relevant_documents(search_results))
