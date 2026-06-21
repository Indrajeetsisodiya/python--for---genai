"""
Exercise 14: Count Messages With Exactly Three Words

Problem:
Count how many messages contain
exactly 3 words.

A word is separated by spaces.

Example:
[
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python is very powerful"
]

Output:
2
"""
# Solution 
def count_messages_with_exactly_three_words(messages):
    count = 0 

    for message in messages:
        a = message.split()
        if len(a) == 3:
            count += 1
    
    return count

# Test case 
total = count_messages_with_exactly_three_words(
 [
    "I love Python",
    "AI is amazing",
    "Hello world",
    "Python is very powerful"
]   
)
print(total)