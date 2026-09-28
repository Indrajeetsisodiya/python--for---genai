'''
Your task:

1. Safely open "rag_raw_14.txt" using with open().
2. Read all lines using .readlines().
3. Remove empty and whitespace-only lines.
4. Create a new file called "rag_cleaned_14.txt".
5. Write only the cleaned lines into the new file.
6. Close the files automatically using with open().
7. Print:

   "RAG document cleaned successfully."

The final file should contain only the useful text lines.

Do not use try/except for this exercise.
'''
with open("rag_raw_14.txt", "r") as file:
    lines = file.readlines()

cleaned_lines = ""
for line in lines:
    if line.strip():
        cleaned_lines += line

with open("rag_cleaned_14.txt", "w") as file:
    file.write(cleaned_lines)
print("Rag document cleaned successfully.")
    

    