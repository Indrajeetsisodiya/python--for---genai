'''
Exercise 14: Prepare High-Quality Chunks for RAG

Problem:
You are building a simplified RAG pipeline.

Your application receives API responses in this structure:

[
    status,
    document_name,
    list_of_chunks
]

Create a function called prepare_high_quality_rag_chunks that:

- Accepts a nested list of API responses.
- Processes only responses where the status is "success".
- Extracts chunks from successful responses.
- Combines all valid chunks into one flat list.
- Removes empty chunks.
- Removes chunks containing only spaces.
- Removes chunks that start with "ERROR:".
- Removes duplicate chunks while preserving the first occurrence.
- Keeps only chunks with 30 or more characters.
- Returns the final cleaned list.

Example:

api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python",
            "Python functions help organize and reuse code effectively",
            "",
            "ERROR: Failed to extract chunk"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information before generating a response",
            "Python functions help organize and reuse code effectively",
            "   "
        ]
    ],
    [
        "error",
        "api.txt",
        [
            "This response should not be processed because the API failed"
        ]
    ],
    [
        "success",
        "embeddings.txt",
        [
            "Embeddings convert meaningful text into numerical vector representations",
            "Short"
        ]
    ]
]

Output:

[
    "Python functions help organize and reuse code effectively",
    "RAG retrieves relevant information before generating a response",
    "Embeddings convert meaningful text into numerical vector representations"
]
'''

# solution
api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python",
            "Python functions help organize and reuse code effectively",
            "",
            "ERROR: Failed to extract chunk"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information before generating a response",
            "Python functions help organize and reuse code effectively",
            "   "
        ]
    ],
    [
        "error",
        "api.txt",
        [
            "This response should not be processed because the API failed"
        ]
    ],
    [
        "success",
        "embeddings.txt",
        [
            "Embeddings convert meaningful text into numerical vector representations",
            "Short"
        ]
    ]
]
def prepare_high_quality_rag_chunks(api_responses):
    cleaned_flat_list = []

    for response in api_responses:
        if response[0] == "success":
            for chunk in response[2]:
                if chunk.strip() and not chunk.startswith("ERROR:"):
                    if len(chunk)>=30:
                        if chunk not in cleaned_flat_list:
                            cleaned_flat_list.append(chunk)

    return cleaned_flat_list

print(prepare_high_quality_rag_chunks(api_responses))

