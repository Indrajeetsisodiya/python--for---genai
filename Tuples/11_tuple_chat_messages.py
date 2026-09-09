'''
Exercise 11: Process Chat Messages

Problem:
A chatbot stores each message as a tuple:

(role, message)

Use the following chat history:

chat_history = [
    ("user", "What is RAG?"),
    ("assistant", "RAG stands for Retrieval-Augmented Generation."),
    ("user", "Why is it useful?"),
    ("assistant", "It allows an LLM to use external information.")
]

Use a `for` loop and tuple unpacking.

Print only the messages sent by the `"user"`.

Expected output:
user: What is RAG?
user: Why is it useful?
'''

# solution
chat_history = [
    ("user", "What is RAG?"),
    ("assistant", "RAG stands for Retrieval-Augmented Generation."),
    ("user", "Why is it useful?"),
    ("assistant", "It allows an LLM to use external information.")
]

for role, message in chat_history:
    if role == "user":
        print(f"{role} : {message}")

