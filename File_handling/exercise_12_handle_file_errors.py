'''
A GenAI application needs to read a document called:

"knowledge_base.txt"

The file might have two possible problems:

1. It doesn't exist.
2. Python doesn't have permission to read it.

Your task:

1. Use try and with open() to read the file.
2. Print the document if it is successfully read.
3. Handle FileNotFoundError and print:

   "Error: Knowledge base file was not found."

4. Handle PermissionError and print:

   "Error: Permission denied while reading the knowledge base."

Use separate except blocks for the two exceptions.
'''

# solution
try:
    with open("knowledge_base.txt", "r") as file:
        document = file.read()
        print(document)

except FileNotFoundError:
    print("Error: Knowledge base file was not found.")

except PermissionError:
    print("Error: Permission denied while reading the knowledge base")