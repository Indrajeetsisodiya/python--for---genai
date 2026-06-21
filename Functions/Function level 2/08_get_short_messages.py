"""
Exercise 8: Get Short Messages

Problem:
Return a list containing all messages
that have less than 10 characters.

Example:

[
    "Hi",
    "Python",
    "This is a long message",
    "Hello"
]

Output:

[
    "Hi",
    "Python",
    "Hello"
]
"""
# Solution
def get_short_messages(messages):
    short_messages = []

    for message in messages:
        if len(message) < 10:
            short_messages.append(message)

    return short_messages

# Test case 
total = get_short_messages([
    "Hi",
    "Python",
    "This is a long message",
    "Hello"
])
print(total)
