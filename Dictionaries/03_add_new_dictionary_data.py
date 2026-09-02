'''
Exercise 3: Add New Information to a Chat Message

Problem:
You are given a dictionary representing a user's chat message:

message = {
    "role": "user",
    "content": "Explain embeddings"
}

The application now needs to store two additional pieces of information:

- "language" → "English"
- "tokens" → 3

Add both key-value pairs to the dictionary.

Then print the entire dictionary.

Expected Output:
{
    "role": "user",
    "content": "Explain embeddings",
    "language": "English",
    "tokens": 3
}
'''

# solution
message = {
    "role": "user",
    "content": "Explain embeddings"
}

message.update({"language": "english", "tokens": 3})
print(message)

