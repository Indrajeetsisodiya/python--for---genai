"""
Exercise 1: Count User Messages

Problem:
Return the total number of messages
in a list without using len().

Example:
["Hi", "Hello", "Bye"] -> 3
"""

# Solution
def count_messages(messages):
    count = 0 

    for _ in messages:
        count +=1 

    return count


total = count_messages(["hi", "hello", "how are you" , "i am indrajeet sisodiya"])
print(total)












