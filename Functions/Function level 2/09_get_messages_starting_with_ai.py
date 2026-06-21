"""
Exercise 9: Get Messages Starting With AI

Problem:
Return a list containing all messages
that start with "AI".

The check should be case-sensitive.

Example:

[
    "AI is amazing",
    "Python is fun",
    "AI can help developers",
    "ai is not counted"
]

Output:

[
    "AI is amazing",
    "AI can help developers"
]
"""
# Solution
def get_messages_starting_with_ai(messages):
    messages_starting_with_ai = []

    for message in messages:
        if message.startswith("AI"):
            messages_starting_with_ai.append(message)

    return messages_starting_with_ai

# Test case 
total = get_messages_starting_with_ai(
 [
    "AI is amazing",
    "Python is fun",
    "AI can help developers",
    "ai is not counted"
]   
)
print(total)
