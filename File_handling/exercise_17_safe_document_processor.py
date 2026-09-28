'''
Create a function called process_document(filename).

The function should:

1. Try to open the given file using with open().
2. Read all lines.
3. Remove empty/whitespace-only lines.
4. Return the cleaned lines.

If the file does not exist:

5. Catch FileNotFoundError.
6. Print:

   "Error: Document not found."

7. Return an empty list.

Then test your function with:

"rag_raw_17.txt"

Print the returned result.
'''

# solution

def process_document(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        cleaned_lines = []
        for line in lines:
            if line.strip():
                cleaned_lines.append(line)
        return cleaned_lines

    except FileNotFoundError:
        print("Error: Document not found.")
        return []

cleaned_lines = process_document("rag_raw_17.txt")
print(cleaned_lines)


