'''
Exercise 14: Process a JSON-Like LLM API Response

Problem:
Your application receives this response:

api_response = {
    "status": "success",
    "results": [
        {
            "id": 1,
            "role": "assistant",
            "content": "RAG retrieves relevant information."
        },
        {
            "id": 2,
            "role": "assistant",
            "content": "The retrieved information is given to the LLM."
        },
        {
            "id": 3,
            "role": "system",
            "content": "Response generated successfully."
        }
    ]
}

Create an empty list called assistant_responses.

Loop through the "results" and add the "content" of every
message whose "role" is "assistant".

Finally, print assistant_responses.

Expected Output:
[
    "RAG retrieves relevant information.",
    "The retrieved information is given to the LLM."
]
'''

# solution
api_response = {
    "status": "success",
    "results": [
        {
            "id": 1,
            "role": "assistant",
            "content": "RAG retrieves relevant information."
        },
        {
            "id": 2,
            "role": "assistant",
            "content": "The retrieved information is given to the LLM."
        },
        {
            "id": 3,
            "role": "system",
            "content": "Response generated successfully."
        }
    ]
}

assistant_responses = []

for response in api_response["results"]:
    if response["role"] == "assistant":
        assistant_responses.append(response["content"])

print(assistant_responses)