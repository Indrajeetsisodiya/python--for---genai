'''
Exercise 5: Extract Information from an API Response

Problem:
An LLM API returns this tuple:

api_response = ("success", "RAG improves document retrieval", 87)

The values represent:

- The API status
- The generated response
- The response token count

Use tuple unpacking to store these three values in separate variables:

- status
- response
- tokens

Then use an `if` statement to check whether the status is `"success"`.

If it is successful, print the response and token count.

Expected output:
RAG improves document retrieval
87
'''

# solution
api_response = ("success", "RAG improves document retrieval", 87)
status,response,tokens = api_response

if status == "success":
    print(response)
    print(tokens)