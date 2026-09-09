'''
Exercise 13: Process Multiple API Responses

Problem:
An application receives several API responses.

Each response is stored as a tuple:

(status_code, response_text)

Use the following data:

api_responses = [
    (200, "Request successful"),
    (404, "Document not found"),
    (200, "Document retrieved"),
    (500, "Server error"),
    (200, "RAG search completed")
]

Loop through the responses using tuple unpacking.

Print only the response text for responses with a status code of `200`.

Expected output:
Request successful
Document retrieved
RAG search completed
'''

# solution
api_responses = [
    (200, "Request successful"),
    (404, "Document not found"),
    (200, "Document retrieved"),
    (500, "Server error"),
    (200, "RAG search completed")
]

for status_role , response_text in api_responses:
    if status_role == 200:
        print(response_text)

