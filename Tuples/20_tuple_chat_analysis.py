'''
Exercise 20: Analyze Chat Messages

Problem:
Each chat message is stored as a tuple:

(role, message, message_length)

Use the following data:

chat_history = [
    ("user", "What is RAG?", 13),
    ("assistant", "RAG connects an LLM with external information.", 45),
    ("user", "How does retrieval work?", 25),
    ("assistant", "Relevant documents are retrieved before generation.", 52),
    ("user", "Is RAG useful?", 14)
]

Create a function called `get_long_user_messages`.

The function should:

1. Receive `chat_history`.
2. Loop through the messages using tuple unpacking.
3. Find messages where:
   - The role is `"user"`
   - The message length is greater than 15
4. Add the entire tuple to a new list.
5. Return the list.

Call the function and print the result.

Expected output:

[('user', 'How does retrieval work?', 25)]

Requirements:
- Use a function.
- Use tuple unpacking.
- Use a loop.
- Use two conditions.
- Store the entire tuple in the result list.
'''

# solution
chat_history = [
    ("user", "What is RAG?", 13),
    ("assistant", "RAG connects an LLM with external information.", 45),
    ("user", "How does retrieval work?", 25),
    ("assistant", "Relevant documents are retrieved before generation.", 52),
    ("user", "Is RAG useful?", 14)
]

def get_long_user_messages(chat_history):
    new_list = []

    for i in chat_history:
        role , message, message_length = i
        if role == "user" and message_length > 15:
            new_list.append(i)

    return new_list

print(get_long_user_messages(chat_history))


        

