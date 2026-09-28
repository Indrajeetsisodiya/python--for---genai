'''
You have a file called "raw_document.txt".

The file contains several lines from a document.
Some lines may be empty.

Example:

Python is useful for AI development.

RAG allows AI systems to use external documents.

Embeddings represent text as numerical vectors.


Your task:

1. Open "raw_document.txt" in read mode.
2. Read all lines using .readlines().
3. Remove empty lines.
4. Save the remaining lines into a new file called
   "cleaned_document.txt".
5. Open "cleaned_document.txt" in write mode.
6. Write each non-empty line into the new file.
7. Close both files.
8. Print:

   "Document cleaned successfully."

Do not use with open() yet.
'''

# solution
read_file = open("raw_document.txt", "r")
lines = read_file.readlines()

non_empty_lines = []
for i in lines:
    if i.strip():
        non_empty_lines.append(i)

non_empty_string = ""
for i in non_empty_lines:
    non_empty_string += i
print(non_empty_string)


write_file = open("cleaned_document.txt","w")
write_file.write((non_empty_string))
read_file.close()
write_file.close()

print("Document cleaned successfully.")
        


