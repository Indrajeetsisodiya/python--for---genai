"""
Exercise 13: Count Messages Containing Both Python and AI

Problem:
Count how many messages contain both
the word "Python" and the word "AI".

The check should be case-sensitive.

Example:
[
    "Python and AI together",
    "I love Python",
    "AI is amazing",
    "Python helps build AI apps"
]

Output:
2
"""
# Solution
def count_messages_containing_both_python_and_ai(messages):
    count = 0

    for message in messages:
        if "Python" in message and "AI" in message:
            count += 1
    
    return count

# Test case 
total = count_messages_containing_both_python_and_ai(
 [
    "Python and AI together",
    "I love Python",
    "AI is amazing",
    "Python helps build AI apps"
]   
)
print(total)
