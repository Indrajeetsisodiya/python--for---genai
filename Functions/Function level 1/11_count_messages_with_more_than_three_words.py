"""
Exercise 11: Count Messages With More Than Three Words

Problem:
In a chatbot application, count how many
messages contain more than 3 words.

A word is separated by spaces.

Example:
[
    "Hello",
    "I love Python",
    "Python is very easy to learn",
    "AI is amazing"
]

Output:
1
"""
# Solution
def count_message_with_more_than_three_words(messages):
    count = 0 

    for message in messages:
        a = message.split()
        if len(a) > 3:
            count  += 1
    return count

# Test case 
total = count_message_with_more_than_three_words(
[
    "Hello",
    "I love Python",
    "Python is very easy to learn",
    "AI is amazing"
]
)
print(total)