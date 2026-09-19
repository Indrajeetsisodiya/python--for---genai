'''
Exercise 10: Handle a missing document

Problem:
Your RAG application needs to read a document called:

knowledge_base.txt

The file might not exist."

Your task:

1. Ask the user for the document filename.
2. Try to open the file in read mode.
3. Catch FileNotFoundError.
4. If the file doesn't exist, print:

Document not found.

5. If the file opens successfully, use else to print:

Document opened successfully.

6. Always use finally to print:

Document access attempt finished.

Important:
Do NOT create the file.
Test your program with a filename that does not exist.

Hint:
open() can raise FileNotFoundError.

# solution
'''
user_input = input("enter the file name: ")
try:
    file = open(user_input , "r")
except FileNotFoundError:
    print("Document not found.")
else:
    print("file opened successfully")
finally:
    print("document access attempt finished.")