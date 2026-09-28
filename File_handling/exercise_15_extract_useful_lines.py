'''
You are preparing a document for a future RAG pipeline.

The document contains useful information mixed with lines
that should be removed.

Your task:

1. Open "rag_document_15.txt" using with open().
2. Read all lines using .readlines().
3. Create an empty list called "useful_lines".
4. Loop through every line.
5. Keep only lines that DO NOT start with:
   - "IGNORE:"
   - "TODO:"
6. Save the useful lines into:
   "rag_useful_15.txt"
7. Write the useful lines into the new file.
8. Print:

   "Useful document created successfully."

9. Finally, open "rag_useful_15.txt" and print its contents
   using .read().

Do not use try/except yet.
'''

# solution
with open("rag_document_15.txt", "r") as file:
    lines = file.readlines()

useful_lines = []
for line in lines:
    if not line.startswith("IGNORE:") and not line.startswith("TODO:"):
        useful_lines.append(line)

userful_lines_str = ""
for i in useful_lines:
    userful_lines_str += i 
 

with open("rag_useful_15.txt", "w") as file:
    file.write(userful_lines_str)

print("Useful document created successfully.")

with open("rag_useful_15.txt", "r") as file:
    print(file.read())

