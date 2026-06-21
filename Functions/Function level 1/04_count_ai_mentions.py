"""
Exercise 4: Count AI Mentions

Problem:
In a collection of chat messages, count how many
messages contain the word "AI".

The check should be case-sensitive.

Example:
[
    "I love AI",
    "Python is fun",
    "AI is changing the world",
    "ai will not count"
]

Output:
2
"""

# Solution

def count_ai_mentions(messages):
    count = 0

    for message in messages:
        if "AI" in message:
            count += 1

    return count

# Test case 
total = count_ai_mentions([
    "I love AI",
    "Python is fun",
    "AI is changing the world",
    "ai will not count"
])
print(total)