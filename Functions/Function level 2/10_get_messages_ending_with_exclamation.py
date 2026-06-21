"""
Exercise 10: Get Messages Ending With Exclamation

Problem:
Return a list containing all messages
that end with an exclamation mark (!).

Example:

[
    "Hello",
    "Amazing!",
    "Python is fun!",
    "How are you?"
]

Output:

[
    "Amazing!",
    "Python is fun!"
]
"""
# Solution 
def get_messages_ending_with_exclamation(messages):
    messages_ending_with_exclamation = []

    for message in messages:
        if message.endswith("!"):
            messages_ending_with_exclamation.append(message)
    
    return messages_ending_with_exclamation

# Test case 
total = get_messages_ending_with_exclamation(
 [
    "Hello",
    "Amazing!",
    "Python is fun!",
    "How are you?"
]   
)
print(total)
