'''
A GenAI application expects a user-uploaded document called:

"user_upload.txt"

The file may not exist.

Your task:

1. Try to open "user_upload.txt" using with open().
2. Read the complete file using .read().
3. Print the document if it exists.
4. Handle FileNotFoundError.
5. If the file does not exist, print:

   "Error: User document was not found."

Do not let the program crash when the file is missing.
'''

# solution
try:
    with open("user_upload.txt", "r") as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print("Error: User document was not found.")