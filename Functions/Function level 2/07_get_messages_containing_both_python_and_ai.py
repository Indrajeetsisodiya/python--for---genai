"""
Exercise 7: Get Messages Containing Both Python and AI

Problem:
Return a list containing all messages
that contain both "Python" and "AI".

The check should be case-sensitive.

Example:

[
    "Python and AI together",
    "I love Python",
    "AI is amazing",
    "Python helps build AI apps"
]

Output:

[
    "Python and AI together",
    "Python helps build AI apps"
]
"""

# Solution
def get_messages_containing_both_python_and_ai(messages):
    messages_containing_both_python_and_ai = []

    for message in messages:
        if "Python" in message and "AI" in message:
            messages_containing_both_python_and_ai.append(message)

    return messages_containing_both_python_and_ai

# Test case 
total = get_messages_containing_both_python_and_ai(
    [
    "Python and AI together",
    "I love Python",
    "AI is amazing",
    "Python helps build AI apps"
]
)
print(total)
