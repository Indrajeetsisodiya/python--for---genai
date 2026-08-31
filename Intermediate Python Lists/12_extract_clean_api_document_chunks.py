'''
Exercise 12: Extract and Clean API Document Chunks

Problem:
You are building a RAG application that receives processed documents
from an API.

The API returns a nested list. Each inner list contains:

[
    status,
    document_name,
    list_of_chunks
]

Only successful responses should be processed.

Create a function called extract_clean_api_document_chunks that:

- Accepts a nested list of API responses.
- Processes only responses where the status is "success".
- Extracts the list of chunks from each successful response.
- Combines chunks from all successful responses into one flat list.
- Removes empty chunks.
- Removes chunks containing only spaces.
- Removes chunks that start with "ERROR:".
- Removes duplicate chunks while preserving the first occurrence.
- Returns the final cleaned flat list.

Example:

api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python uses indentation",
            "",
            "Functions allow code reuse"
        ]
    ],
    [
        "error",
        "api.txt",
        [
            "ERROR: API request failed"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information",
            "Functions allow code reuse",
            "   "
        ]
    ],
    [
        "success",
        "embeddings.txt",
        [
            "Embeddings convert text into vectors",
            "ERROR: Invalid chunk"
        ]
    ]
]

Output:

[
    "Python uses indentation",
    "Functions allow code reuse",
    "RAG retrieves relevant information",
    "Embeddings convert text into vectors"
]
'''

# solution
api_responses = [
    [
        "success",
        "python.txt",
        [
            "Python uses indentation",
            "",
            "Functions allow code reuse"
        ]
    ],
    [
        "error",
        "api.txt",
        [
            "ERROR: API request failed"
        ]
    ],
    [
        "success",
        "rag.txt",
        [
            "RAG retrieves relevant information",
            "Functions allow code reuse",
            "   "
        ]
    ],
    [
        "success",
        "embeddings.txt",
        [
            "Embeddings convert text into vectors",
            "ERROR: Invalid chunk"
        ]
    ]
]
def extract_clean_api_document_chunks(api_responses):
    cleaned_flat_list = []

    for i in api_responses:
        if i[0] == "success":
            for j in i[2]:
                if j.strip() and not j.startswith("ERROR:"):
                    if j not in cleaned_flat_list:
                        cleaned_flat_list.append(j)
    return cleaned_flat_list
                  

print(extract_clean_api_document_chunks(api_responses))