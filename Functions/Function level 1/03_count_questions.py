"""
Exercise 3: Count Questions

Problem:
In a chatbot conversation, some messages
are questions and some are not.

Write a function that returns the number
of messages that end with a question mark (?).

Example:
[
    "Hello",
    "How are you?",
    "Tell me a joke",
    "What is Python?"
]

Output:
2
"""
def count_questions(questions):
    count = 0

    for question in questions:
        if question.endswith('?'):
            count += 1

    return count


# Test case
result = count_questions([
    "Hello",
    "How are you?",
    "Tell me a joke",
    "What is Python?"
])
print(result)
