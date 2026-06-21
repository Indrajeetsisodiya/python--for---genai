"""
Exercise 5: Get Messages With More Than Three Words

Problem:
Return a list containing all messages
that have more than 3 words.

A word is separated by spaces.

Example:

[
    "Hello",
    "I love Python",
    "Python is very easy to learn",
    "AI is amazing"
]

Output:

[
    "Python is very easy to learn"
]
"""

# Solution 
def get_messages_with_more_than_three_words(messages):
    messages_with_more_than_three_words = []

    for message in messages:
        if len(message.split()) > 3:
            messages_with_more_than_three_words.append(message)
    
    return messages_with_more_than_three_words

# Test case 
total = get_messages_with_more_than_three_words(
 [
    "Hello",
    "I love Python",
    "Python is very easy to learn",
    "AI is amazing"
]   
)
print(total)

