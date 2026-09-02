'''
Exercise 1: Create and Access a Chat Message

Problem:
Create a dictionary called message that represents a chat message.

It should contain:

- "role" with the value "user"
- "content" with the value "What is RAG?"
- "language" with the value "English"

Then print:

1. The value of "role"
2. The value of "content"

Do not print the entire dictionary.

Example:
message = {
    "role": "user",
    "content": "What is RAG?",
    "language": "English"
}

Output:
user
What is RAG?
'''

# solution
message = {"role": "user" , "content": "What is RAG?", "language": "English"}

# one way of printing the values
# print(message.get("role"))
# print(message.get("content"))

# another way 
print(message["role"])
print(message["content"])