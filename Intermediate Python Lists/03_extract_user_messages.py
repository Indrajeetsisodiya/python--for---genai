'''
Exercise 3: Extract Useful User Messages

Problem:
You are building a simple chat application.

The application stores messages as a list of lists.
Each inner list contains:

[
    role,
    message
]

Example:

messages = [
    ["system", "You are a helpful AI assistant"],
    ["user", "Explain Python functions"],
    ["assistant", "A function is reusable code"],
    ["user", ""],
    ["user", "What is RAG?"],
    ["assistant", "RAG combines retrieval with generation"],
    ["user", "   "],
    ["user", "How do APIs work?"]
]

Create a function called extract_user_messages that:

- Accepts a nested list of messages.
- Extracts only messages where the role is "user".
- Removes empty messages.
- Removes messages containing only spaces.
- Returns a new list containing only valid user messages.
- Preserves the original order.

Output:

[
    "Explain Python functions",
    "What is RAG?",
    "How do APIs work?"
]
'''

# solution
messages = [
    ["system", "You are a helpful AI assistant"],
    ["user", "Explain Python functions"],
    ["assistant", "A function is reusable code"],
    ["user", ""],
    ["user", "What is RAG?"],
    ["assistant", "RAG combines retrieval with generation"],
    ["user", "   "],
    ["user", "How do APIs work?"]
]

def extract_user_messages(messages):
    valid_user_messages = []

    for message in messages:
        if message[0] == "user" and message[1].strip():
            valid_user_messages.append(message[1])
            
    return valid_user_messages


print(extract_user_messages(messages))