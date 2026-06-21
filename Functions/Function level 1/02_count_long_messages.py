"""
Exercise 2: Count Long Chat Messages

Problem:
A message is considered long if it contains
more than 20 characters.

Write a function that returns the number
of long messages in a list.

Example:
[
    "Hi",
    "Can you explain Python functions?",
    "Thanks"
]

Output:
1
"""

# Solution
def count_long_messages(messages):
    count = 0

    for message in messages:
        if len(message) > 20:
            count += 1

    return count

#Test case
total_msg= count_long_messages(["hi" , "this is indrajeet sisodiya writing code for my second problem " , "this is genAI problem", "hi this is another text i am writing to test "])
print(total_msg)
