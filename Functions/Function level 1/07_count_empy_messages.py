"""
Exercise 7: Count Empty Messages

Problem:
In a chatbot application, some messages
may be empty strings.

Write a function that returns the number
of empty messages in a list.

An empty message looks like:

""

Example:
[
    "Hello",
    "",
    "Python",
    "",
    "AI"
]

Output:
2
"""
# Solution
def count_empty_messages(messages):
    count = 0 

    for message in messages:
        if message == "":
            count += 1
    
    return count

# Test case
total = count_empty_messages(
    [
    "Hello",
    "",
    "Python",
    "",
    "AI"
]
)
print(total)
