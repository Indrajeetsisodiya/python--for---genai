'''
Exercise 10: Extract Data from an API Response

Problem:
An API returns the following response:

api_response = {
    "status": "success",
    "data": {
        "model": "gpt-5",
        "response": "RAG improves responses by retrieving relevant information.",
        "tokens": 18
    }
}

Extract and print:

1. The model name
2. The response text
3. The number of tokens

Expected Output:
gpt-5
RAG improves responses by retrieving relevant information.
18
'''

# solution
api_response = {
    "status": "success",
    "data": {
        "model": "gpt-5",
        "response": "RAG improves responses by retrieving relevant information.",
        "tokens": 18
    }
}

print(api_response["data"]["model"])
print(api_response["data"]["response"])
print(api_response["data"]["tokens"])
