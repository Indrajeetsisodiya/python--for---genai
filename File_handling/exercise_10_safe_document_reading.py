'''
You have a file called "user_document.txt".

The file contains text uploaded by a user.

Your task:

1. Open the file using `with open()`.
2. Use read mode.
3. Read the entire document using .read().
4. Store the content in a variable called "document".
5. Print the document.
6. Do NOT use .close().

The purpose of this exercise is to practice safe file handling
using a context manager.
'''

# solution
with open("user_document.txt","r") as file:
    text = file.read()
    print(text)


