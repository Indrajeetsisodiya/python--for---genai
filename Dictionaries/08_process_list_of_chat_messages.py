'''
Exercise 8: Process a List of Chat Messages

Problem:
You receive these chat messages from an API:

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
        "content": "Why is it useful?"
    }
]

Use a loop to print only the "content" of each message.

Expected Output:
What is RAG?
RAG stands for Retrieval-Augmented Generation.
Why is it useful?
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
        "content": "Why is it useful?"
    }
]

for message in messages:
    print(message["content"])
