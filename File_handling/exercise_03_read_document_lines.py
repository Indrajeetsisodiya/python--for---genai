'''
You have a file called "rag_document.txt".

The file contains 5 lines of information about RAG.

Your task:

1. Open "rag_document.txt" in read mode.
2. Read all lines using .readlines().
3. Store the result in a variable called "lines".
4. Print the list.
5. Close the file.

Do not use .read() or .readline().
'''

# solution
f = open("rag_document.txt", "r")
text = f.readlines()
print(text)
f.close()

