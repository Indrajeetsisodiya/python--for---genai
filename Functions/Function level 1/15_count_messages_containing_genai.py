"""
Exercise 15: Count Messages Containing GenAI

Problem:
Count how many messages contain
the word "GenAI".

The check should be case-sensitive.

Example:
[
    "I want to learn GenAI",
    "Python is fun",
    "GenAI applications are growing",
    "genai is not counted"
]

Output:
2
"""
# Solution 
def count_messages_containing_genai(messages):
    count = 0 

    for message in messages:
        if "GenAI" in message:
            count += 1
    
    return count

# Test case 
total = count_messages_containing_genai(
    [
    "I want to learn GenAI",
    "Python is fun",
    "GenAI applications are growing",
    "genai is not counted"
]
)
print(total)
