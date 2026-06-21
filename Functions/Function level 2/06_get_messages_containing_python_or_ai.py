"""
Exercise 6: Get Messages Containing Python or AI

Problem:
Return a list containing all messages
that contain either "Python" or "AI".

The check should be case-sensitive.

Example:

[
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python and AI together"
]

Output:

[
    "I love Python",
    "AI is amazing",
    "Python and AI together"
]
"""
# Solution
def get_messages_containing_python_or_ai(messages):
    messages_containing_python_or_ai = []

    for message in messages:
        if "Python" in message or "AI" in message:
            messages_containing_python_or_ai.append(message)

    return messages_containing_python_or_ai

# Test case 
total = get_messages_containing_python_or_ai(
  [
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python and AI together"
]  
)
print(total)
