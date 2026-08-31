'''
Exercise 8: Find the Shortest Useful Document Chunk

Problem:
You are checking document chunks before sending them to an AI application.

Create a function called find_shortest_document_chunk that:

- Accepts a list of document chunks.
- Finds the shortest valid chunk.
- Ignores empty strings.
- Ignores strings containing only spaces.
- Returns the shortest valid chunk.

Example:

chunks = [
    "",
    "   ",
    "API",
    "Python functions allow code reuse",
    "RAG retrieves relevant information before generation",
    "LLM"
]

Output:

"API"
'''

# solution
chunks = [
    "",
    "   ",
    "Python functions allow code reuse",
    "RAG retrieves relevant information before generation",
    "API",
    "LLM"
]

def find_shortest_chunk(chunks):
    shortest_chunk = None

    for chunk in chunks:
        if chunk.strip():
            if shortest_chunk is None or len(shortest_chunk) > len(chunk):
                shortest_chunk = chunk
    return shortest_chunk

print(find_shortest_chunk(chunks))


