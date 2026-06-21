"""
Exercise 4: Get Messages With Numbers

Problem:
Return a list containing all messages
that contain at least one digit.

Example:

[
    "Hello",
    "My age is 21",
    "Python",
    "I have 2 dogs"
]

Output:

[
    "My age is 21",
    "I have 2 dogs"
]
"""
# Solution 
def get_messages_with_numbers(messages):
    message_with_numbers = []

    for message in messages:
        if any(char.isdigit() for char in message ):
            message_with_numbers.append(message)
    
    return message_with_numbers

# Test case 
total  = get_messages_with_numbers(
 [
    "Hello",
    "My age is 21",
    "Python",
    "I have 2 dogs"
]   
)
print(total)
