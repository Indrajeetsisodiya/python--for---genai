'''
Exercise 7: Find the Longest Document Chunk

Problem:
You are preparing document chunks for an AI application.

Some chunks contain more detailed information than others.

Create a function called find_longest_document_chunk that:

- Accepts a list of document chunks.
- Finds the chunk containing the most characters.
- Ignores empty strings.
- Ignores strings containing only spaces.
- Returns the longest valid chunk.

Example:

chunks = [
    "",
    "API",
    "Python functions allow you to organize and reuse code",
    "   ",
    "RAG retrieves relevant documents before sending information to an LLM",
    "Embeddings convert text into numerical vectors"
]

Output:

"RAG retrieves relevant documents before sending information to an LLM"
'''

# solution
chunks = [
    "",
    "API",
    "Python functions allow you to organize and reuse code",
    "   ",
    "RAG retrieves relevant documents before sending information to an LLM",
    "Embeddings convert text into numerical vectors"
]

def find_longest_document_chunk(chunks):
    longest_document_chunk_list = chunks[0]

    for chunk in chunks:
        if chunk.strip():
            if len(longest_document_chunk_list) < len(chunk):
                        longest_document_chunk_list = chunk
        

    return longest_document_chunk_list
 
print(find_longest_document_chunk(chunks))
 



