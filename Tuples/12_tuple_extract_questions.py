'''
Exercise 12: Extract User Questions

Problem:
You have a chatbot conversation stored as a list of tuples.

Each tuple contains:

(role, message)

Use the following data:

chat_history = [
    ("user", "What is Python?"),
    ("assistant", "Python is a programming language."),
    ("user", "What is a tuple?"),
    ("assistant", "A tuple is an immutable collection."),
    ("user", "Where are tuples useful?")
]

Create an empty list called `questions`.

Loop through the chat history using tuple unpacking.

If the role is `"user"`, add the message to the `questions` list.

Finally, print the `questions` list.

Expected output:
['What is Python?', 'What is a tuple?', 'Where are tuples useful?']
'''

# solution
chat_history = [
    ("user", "What is Python?"),
    ("assistant", "Python is a programming language."),
    ("user", "What is a tuple?"),
    ("assistant", "A tuple is an immutable collection."),
    ("user", "Where are tuples useful?")
]

questions = []

for role , message in chat_history:
    if role == "user":
        questions.append(message)

print(questions)
