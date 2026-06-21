"""
Exercise 1: Get Long Messages

Problem:
Instead of counting long messages,
return a list containing all messages
that have more than 20 characters.

Example:

[
    "Hi",
    "Can you explain Python functions?",
    "Thanks"
]

Output:

[
    "Can you explain Python functions?"
]
"""
# Solution
def get_long_messages(messages):
    long_messages = []

    for message in messages:
        if len(message) >20:
            long_messages.append(message)
    
    return long_messages

# Test case 
total = get_long_messages(
  [
    "Hi",
    "Can you explain Python functions?",
    "Thanks"
]  
)
print(total)
