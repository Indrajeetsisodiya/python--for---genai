"""
Exercise 8: Count Excited Messages

Problem:
In a chatbot conversation, some messages
show excitement by ending with an exclamation mark (!).

Write a function that returns the number
of messages that end with "!".

Example:
[
    "Hello",
    "Amazing!",
    "Python is fun!",
    "How are you?"
]

Output:
2
"""
# Solution
def count_exclamation_messages(messages):
    count = 0 

    for message in messages:
        if message.endswith("!"):
            count += 1

    return count

# Test case
total = count_exclamation_messages(
[
    "Hello",
    "Amazing!",
    "Python is fun!",
    "How are you?"
]
)
print(total)