'''
Exercise 11: Extract Successful API Documents

Problem:
You are building an AI application that receives document data from an API.

The API returns a nested list. Each inner list contains:

[
    status,
    document_name,
    document_text
]

Some API responses failed and should not be used.

Create a function called extract_successful_api_documents that:

- Accepts a nested list of API responses.
- Keeps only responses where the status is "success".
- Extracts only the document_text.
- Removes empty document texts.
- Removes document texts containing only spaces.
- Removes duplicate document texts while preserving the first occurrence.
- Returns a flat list containing the cleaned document texts.

Example:

api_responses = [
    ["success", "python.txt", "Python functions help organize reusable code"],
    ["error", "api.txt", "ERROR: API request failed"],
    ["success", "rag.txt", "RAG retrieves relevant information"],
    ["success", "backup.txt", "Python functions help organize reusable code"],
    ["success", "empty.txt", ""],
    ["error", "database.txt", "Connection failed"],
    ["success", "embeddings.txt", "Embeddings convert text into vectors"]
]

Output:

[
    "Python functions help organize reusable code",
    "RAG retrieves relevant information",
    "Embeddings convert text into vectors"
]
'''

# solution
api_responses = [
    ["success", "python.txt", "Python functions help organize reusable code"],
    ["error", "api.txt", "ERROR: API request failed"],
    ["success", "rag.txt", "RAG retrieves relevant information"],
    ["success", "backup.txt", "Python functions help organize reusable code"],
    ["success", "empty.txt", ""],
    ["error", "database.txt", "Connection failed"],
    ["success", "embeddings.txt", "Embeddings convert text into vectors"]
]

def extract_successful_api_documents(api_responses):
    cleaned_document = []

    for i in api_responses:
        if i[0] == "success":
                j = i[2]
                if j not in cleaned_document and j.strip():
                    cleaned_document.append(j)

    return cleaned_document

print(extract_successful_api_documents(api_responses))