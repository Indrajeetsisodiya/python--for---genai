'''
Exercise 3: Process Chat Metadata

Problem:
You have a tuple containing information about a chat message:

message_data = ("user", "Explain RAG", 42)

The values represent:

- The role of the sender
- The message text
- The number of words in the message

Use a `for` loop to print each value in the tuple.

Expected output:
user
Explain RAG
42
'''

# solution
message_data = ("user", "Explain RAG", 42)

for data in message_data:
    print(data)
