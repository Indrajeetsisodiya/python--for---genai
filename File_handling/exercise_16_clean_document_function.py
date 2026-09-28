'''
Create a function called clean_document(filename).

The function should:

1. Open the given file using with open().
2. Read all lines using .readlines().
3. Remove empty and whitespace-only lines.
4. Return the cleaned lines as a list.

Then:

5. Call the function using "rag_raw_16.txt".
6. Store the returned result in a variable called "cleaned_lines".
7. Print the cleaned lines.
8. Print the number of cleaned lines.

Do not create a new output file in this exercise.

The goal is to turn document cleaning into a reusable function.
'''

# solution
def clean_document(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        if line.strip():
            cleaned_lines.append(line)

    return cleaned_lines

cleaned_lines = clean_document("rag_raw_16.txt")
print(cleaned_lines)




    