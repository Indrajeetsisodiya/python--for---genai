'''
A user uploads a document called "genai_upload_13.txt".

The document may contain:
- Normal text lines
- Empty lines
- Lines containing only spaces

Your task:

1. Safely open the file using with open().
2. Read all lines using .readlines().
3. Create an empty list called "cleaned_lines".
4. Loop through every line.
5. Remove empty/whitespace-only lines.
6. Add the remaining lines to cleaned_lines.
7. Print:

   "Original lines: X"
   "Cleaned lines: Y"

8. Handle FileNotFoundError and print:

   "Error: User document was not found."

Do NOT write the cleaned document to another file yet.
'''

# solution
try:
   with open("genai_upload_13.txt", "r") as file:
      lines = file.readlines()

   cleaned_lines = []
   for line in lines:
      if line.strip():
         cleaned_lines.append(line)

   print(f"Original lines: {len(lines)}")
   print(f"Cleaned lines: {len(cleaned_lines)}")

except FileNotFoundError:
   print("Error: User document was not found.")



