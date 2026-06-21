"""
Exercise 12: Count Messages Containing Python or AI

Problem:
Count how many messages contain either
the word "Python" or the word "AI".

The check should be case-sensitive.

Example:
[
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python and AI together"
]

Output:
3
"""
# Solution 
def count_messages_containing_Python_or_AI(messages):
    count = 0 

    for message in messages:
        if "Python" in message or "AI" in message:
            count += 1

    return count

# Test case
total = count_messages_containing_Python_or_AI(
[
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python and AI together"
]
)
print(total)