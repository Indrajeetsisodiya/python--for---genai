'''
Exercise 16: Count Successful API Responses

Problem:
An application receives multiple API responses.

Each response is represented by a tuple:

(status_code, response_text)

Use this data:

api_responses = [
    (200, "Request successful"),
    (404, "Document not found"),
    (200, "Document retrieved"),
    (500, "Server error"),
    (200, "RAG search completed"),
    (401, "Unauthorized"),
    (200, "Response generated")
]

Create a function called `count_successful_responses`.

The function should:

1. Receive `api_responses`.
2. Loop through the responses using tuple unpacking.
3. Count how many responses have a status code of `200`.
4. Return the count.

Call the function and print the result.

Expected output:
4
'''

# solution
api_responses = [
    (200, "Request successful"),
    (404, "Document not found"),
    (200, "Document retrieved"),
    (500, "Server error"),
    (200, "RAG search completed"),
    (401, "Unauthorized"),
    (200, "Response generated")
]

def count_successful_responses(api_responses):
    count = 0 
    for status_code , _ in api_responses:
        if status_code == 200:
            count += 1
    return count

print(count_successful_responses(api_responses))




