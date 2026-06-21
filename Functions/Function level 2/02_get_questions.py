"""
Exercise 2: Get Questions

Problem:
Instead of counting questions,
return a list containing all messages
that end with a question mark (?).

Example:

[
    "Hello",
    "How are you?",
    "Tell me a joke",
    "What is Python?"
]

Output:

[
    "How are you?",
    "What is Python?"
]
"""
# Solution 
def get_questions(messages):
    questions = []

    for message in messages:
        if message.endswith("?"):
            questions.append(message)
    
    return questions

# Test case 
total = get_questions(
    [
    "Hello",
    "How are you?",
    "Tell me a joke",
    "What is Python?"
]
)
print(total)
