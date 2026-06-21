"""
Exercise 10: Count Messages Containing Numbers

Problem:
In a chatbot application, users sometimes
send messages containing numbers.

Write a function that returns the number
of messages that contain at least one digit.

Example:
[
    "Hello",
    "My age is 21",
    "Python",
    "I have 2 dogs"
]

Output:
2
"""
# Solution
def count_messages_containing_numbers(messages):
    count = 0 

    for message in messages:
        if any(char.isdigit() for char in message):  
            count += 1

    return count

# Test case 
total = count_messages_containing_numbers(
    [
    "Hello",
    "My age is 21",
    "Python",
    "I have 2 dogs"
]
)
print(total)

