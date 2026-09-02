'''
Exercise 9: Extract User Messages

Problem:
You receive a chat history:

messages = [
    {
        "role": "user",
        "content": "What is RAG?"
    },
    {
        "role": "assistant",
        "content": "RAG stands for Retrieval-Augmented Generation."
    },
    {
        "role": "user",
        "content": "How does it work?"
    },
    {
        "role": "assistant",
        "content": "It retrieves relevant information before generating an answer."
    }
]

Create an empty list called user_messages.

Loop through the messages and add only the content of messages
where the "role" is "user" to user_messages.

Finally, print user_messages.

Expected Output:
["What is RAG?", "How does it work?"]
'''

# solution
messages = [
    {
        "role": "user",
        "content": "What is RAG?"
    },
    {
        "role": "assistant",
        "content": "RAG stands for Retrieval-Augmented Generation."
    },
    {
        "role": "user",
        "content": "How does it work?"
    },
    {
        "role": "assistant",
        "content": "It retrieves relevant information before generating an answer."
    }
]

user_messages = []

for message in messages:
    if message["role"] == "user":
        user_messages.append(message["content"])
print(user_messages)
