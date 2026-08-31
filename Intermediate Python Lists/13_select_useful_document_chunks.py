'''
Exercise 13: Select the Most Useful Document Chunks

Problem:
You are preparing cleaned document chunks for a RAG application.

You have a list of document chunks, but very short chunks are often not
useful because they may not contain enough context.

Create a function called select_useful_document_chunks that:

- Accepts a list of document chunks.
- Removes empty chunks.
- Removes chunks containing only spaces.
- Removes chunks that start with "ERROR:".
- Removes duplicate chunks while preserving the first occurrence.
- Keeps only chunks with 20 or more characters.
- Returns the final cleaned list.

Example:

chunks = [
    "",
    "API",
    "Python functions help organize reusable code",
    "   ",
    "ERROR: Failed to process chunk",
    "RAG retrieves relevant information before generation",
    "Python functions help organize reusable code",
    "Short text",
    "Embeddings convert text into numerical vectors"
]

Output:

[
    "Python functions help organize reusable code",
    "RAG retrieves relevant information before generation",
    "Embeddings convert text into numerical vectors"
]
'''

# solution
chunks = [
    "",
    "API",
    "Python functions help organize reusable code",
    "   ",
    "ERROR: Failed to process chunk",
    "RAG retrieves relevant information before generation",
    "Python functions help organize reusable code",
    "Short text",
    "Embeddings convert text into numerical vectors"
]

def select_useful_document_chunks(chunks):
    useful_chunks = []

    for chunk in chunks:
        if chunk.strip() and not chunk.startswith("ERROR:"):
            if len(chunk) >= 20:
                if chunk not in useful_chunks:
                    useful_chunks.append(chunk)
    return useful_chunks

print(select_useful_document_chunks(chunks))
                