'''
Exercise 15: Build the Final RAG Context List

Problem:
You are building the final preprocessing step before sending document
chunks to a RAG application.

Your application receives API responses in this structure:

[
    status,
    document_name,
    list_of_chunks
]

Create a function called build_final_rag_context that:

- Accepts a nested list of API responses.
- Processes only responses where the status is "success".
- Extracts chunks from successful responses.
- Combines all chunks into one flat list.
- Removes empty chunks.
- Removes chunks containing only spaces.
- Removes chunks that start with "ERROR:".
- Removes duplicate chunks while preserving the first occurrence.
- Keeps only chunks with 25 or more characters.
- Finds the longest valid chunk.
- Finds the shortest valid chunk.
- Returns a list containing:

[
    cleaned_chunks,
    longest_chunk,
    shortest_chunk
]

Example:

api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python functions organize reusable code",
            "",
            "Functions are useful"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information before generating an answer",
            "Python functions organize reusable code",
            "   "
        ]
    ],
    [
        "error",
        "failed.txt",
        [
            "This response should be ignored completely"
        ]
    ],
    [
        "success",
        "api.txt",
        [
            "APIs allow different applications to communicate with each other",
            "ERROR: Invalid document chunk"
        ]
    ]
]

Output:

[
    [
        "Python functions organize reusable code",
        "RAG retrieves relevant information before generating an answer",
        "APIs allow different applications to communicate with each other"
    ],
    "RAG retrieves relevant information before generating an answer",
    "Python functions organize reusable code"
]
'''

# solution
api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python functions organize reusable code",
            "",
            "Functions are useful"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information before generating an answer",
            "Python functions organize reusable code",
            "   "
        ]
    ],
    [
        "error",
        "failed.txt",
        [
            "This response should be ignored completely"
        ]
    ],
    [
        "success",
        "api.txt",
        [
            "APIs allow different applications to communicate with each other",
            "ERROR: Invalid document chunk"
        ]
    ]
]

def build_final_rag_context(api_responses):
    cleaned_chunks = []
    shortest_chunk = None
    longest_chunk = ""


    for i in api_responses:
        if i[0] == "success":
            for j in i[2]:
                if j.strip() and not j.startswith("ERROR:"):
                    if len(j) >= 25:
                        if j not in cleaned_chunks:
                            cleaned_chunks.append(j)

    for chunk in cleaned_chunks:
        if len(chunk) > len(longest_chunk):
            longest_chunk = chunk
    
        if shortest_chunk is None or len(chunk) < len(shortest_chunk):
            shortest_chunk = chunk
                            

    return [cleaned_chunks,longest_chunk,shortest_chunk]

print(build_final_rag_context(api_responses))




  

