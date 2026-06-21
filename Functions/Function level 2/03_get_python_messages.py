"""
Exercise 3: Get Python Messages

Problem:
Return a list containing all messages
that contain the word "Python".

The check should be case-sensitive.

Example:

[
    "I love Python",
    "AI is amazing",
    "python is fun",
    "Python functions are useful"
]

Output:

[
    "I love Python",
    "Python functions are useful"
]
"""
# Solution 
def get_python_messages(messages):
    python_messages = []

    for message in messages:
        if "Python" in message:
            python_messages.append(message)
    
    return python_messages

# Test case 
total = get_python_messages(
    [
    "I love Python",
    "AI is amazing",
    "python is fun",
    "Python functions are useful"
]
)
print(total)
