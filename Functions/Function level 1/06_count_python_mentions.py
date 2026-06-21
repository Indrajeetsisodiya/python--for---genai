"""
Exercise 6: Count Python Mentions

Problem:
In a list of messages, count how many
messages contain the word "Python".

The check should be case-sensitive.

Example:
[
    "I am learning Python",
    "python is fun",
    "Python functions are useful",
    "I like coding"
]

Output:
2
"""
# Solution
def count_python_mentions(messages):
    count = 0 
    
    for message in messages:
        if "Python" in message:
            count += 1

    return count

# Test case 
total = count_python_mentions([
    "I am learning Python",
    "python is fun",
    "Python functions are useful",
    "I like coding"
])
print(total)