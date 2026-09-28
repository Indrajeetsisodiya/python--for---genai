'''
You have a file called "document.txt".

The file contains several lines of text from a document
that will eventually be used in a RAG pipeline.

Your task:

1. Open "document.txt" in read mode.
2. Read all lines using .readlines().
3. Store the lines in a variable called "lines".
4. Use len() to find how many lines the document contains.
5. Print:
   "The document contains X lines."
6. Close the file.

Use concepts you already know:
- open()
- readlines()
- len()
- print()
- close()
'''

# solution
f = open("document.txt", "r")
lines = f.readlines()
length = (len(lines))
print(f"The document contains {length} lines.")
f.close()

