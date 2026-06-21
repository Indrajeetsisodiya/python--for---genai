"""
Exercise 5: Count Short Messages

Problem:
A message is considered short if it contains
less than 10 characters.

Write a function that returns the number
of short messages in a list.

Example:
[
    "Hi",
    "Python",
    "This is a long message",
    "Hello"
]

Output:
3
"""

# Solution
def count_short_messages(messages):
    count = 0 

    for message in messages:
        if len(message) < 10:
            count += 1 

    return count

# Test case 
total = count_short_messages([
    "Hi",
    "Python",
    "This is a long message",
    "Hello"
])
print(total)