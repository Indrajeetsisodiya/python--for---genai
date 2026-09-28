'''
You have a file called "rag_notes.txt".

The file contains several lines of notes about RAG.

Your task:

1. Open "rag_notes.txt" in read mode.
2. Read ONLY the first line using .readline().
3. Print that line.
4. Close the file.

Do not use .read() for this exercise.
'''

# solution
f = open("rag_notes.txt", "r")
text = f.readline()
print(text)
f.close()
