'''
Exercise 4: Clean Invalid API Responses

Problem:
You are building an AI application that receives a list of responses
from an external API.

Some responses are not useful and should be removed.

Create a function called clean_api_responses that:

- Accepts a list of responses.
- Removes empty strings.
- Removes responses containing only spaces.
- Removes duplicate responses while preserving the first occurrence.
- Removes responses that start with "ERROR:".
- Returns a cleaned list.

Example:

responses = [
    "Python is a programming language",
    "",
    "ERROR: API rate limit exceeded",
    "What is RAG?",
    "Python is a programming language",
    "   ",
    "ERROR: Invalid request",
    "Embeddings convert text into vectors",
    "What is RAG?"
]

Output:

[
    "Python is a programming language",
    "What is RAG?",
    "Embeddings convert text into vectors"
]
'''

# solution
responses = [
    "Python is a programming language",
    "",
    "ERROR: API rate limit exceeded",
    "What is RAG?",
    "Python is a programming language",
    "   ",
    "ERROR: Invalid request",
    "Embeddings convert text into vectors",
    "What is RAG?"
]
def clean_api_responses(responses):
    valid_api_responses = []

    for i in responses:
        if i.strip() and not i.startswith("ERROR:"):
            if i not in valid_api_responses:
                valid_api_responses.append(i)

    return valid_api_responses

print(clean_api_responses(responses))
