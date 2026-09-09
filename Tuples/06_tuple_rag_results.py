'''
Exercise 6: Process RAG Search Results

Problem:
A RAG system returns search results as tuples.

Each tuple contains:

(document_id, similarity_score)

Use the following data:

search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.81),
    ("doc_309", 0.95)
]

Use a `for` loop and tuple unpacking to process each result.

For every result:

- Extract the document ID into `document_id`
- Extract the similarity score into `score`
- Print the document ID and score

Expected output:
doc_101 0.92
doc_205 0.81
doc_309 0.95
'''

# solution
search_results = [
    ("doc_101", 0.92),
    ("doc_205", 0.81),
    ("doc_309", 0.95)
]

for document_id , similarity_score in search_results:
    print(document_id, similarity_score)
    


    
