'''
Exercise 6: Flatten Document Chunks

Problem:
You are preparing documents for an AI application.

The document chunks are grouped by document in a nested list.

Example:

document_chunks = [
    [
        "Python uses indentation",
        "Functions help organize code"
    ],
    [
        "APIs allow applications to communicate",
        "JSON is commonly used in APIs"
    ],
    [
        "RAG retrieves relevant documents",
        "Embeddings represent text as vectors"
    ]
]

Create a function called flatten_document_chunks that:

- Accepts a nested list of document chunks.
- Combines all inner lists into one single list.
- Preserves the original order of the chunks.
- Returns the flattened list.

Output:

[
    "Python uses indentation",
    "Functions help organize code",
    "APIs allow applications to communicate",
    "JSON is commonly used in APIs",
    "RAG retrieves relevant documents",
    "Embeddings represent text as vectors"
]
'''

# solution
document_chunks = [
    [
        "Python uses indentation",
        "Functions help organize code"
    ],
    [
        "APIs allow applications to communicate",
        "JSON is commonly used in APIs"
    ],
    [
        "RAG retrieves relevant documents",
        "Embeddings represent text as vectors"
    ]
]
def flatten_document_chunks(document_chunks):
    flattened_chunks = []

    for document in document_chunks:
        for chunk in document:
            flattened_chunks.append(chunk)
    return flattened_chunks

print(flatten_document_chunks(document_chunks))