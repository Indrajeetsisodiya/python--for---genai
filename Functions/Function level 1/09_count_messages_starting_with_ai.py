"""
Exercise 9: Count Messages Starting With AI

Problem:
In a list of messages, count how many
messages start with the word "AI".

The check should be case-sensitive.

Example:
[
    "AI is amazing",
    "Python is fun",
    "AI can help developers",
    "ai is not counted"
]

Output:
2
"""
# Solution
def count_messages_starting_with_ai(messages):
    count = 0 

    for message in messages:
        if message.startswith("AI"):
            count += 1
    
    return count

total = count_messages_starting_with_ai(
[
    "AI is amazing",
    "Python is fun",
    "AI can help developers",
    "ai is not counted"
]
)
print(total)