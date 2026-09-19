'''
Exercise 2: Handle a missing dictionary key

Problem:
An AI API returns information about a response.

Sometimes the API response contains an "answer" key,
but sometimes that key is missing.

Your task:

1. Try to access the "answer" key from the dictionary.
2. Store its value in a variable called answer.
3. Catch the appropriate exception if the key does not exist.
4. If the key is missing, print:

AI response did not contain an answer.

Use this dictionary:

response = {
    "status": "success",
    "model": "my-ai-model"
}

Expected output:

AI response did not contain an answer.

Hint:
Trying to access a dictionary key that doesn't exist
causes a KeyError.

# solution
'''

response = {
    "status": "success",
    "model": "my-ai-model"
}

try:
    answer = response["answer"]

except KeyError:
    print("AI response did not contain an answer")
else:
    print(answer)


