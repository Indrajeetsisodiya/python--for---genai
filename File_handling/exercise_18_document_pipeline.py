'''
Create a function called prepare_document(input_file, output_file).

The function should:

1. Try to open input_file using with open().
2. Read all lines.
3. Remove empty/whitespace-only lines.
4. Open output_file using with open() in write mode.
5. Write the cleaned lines into the output file.
6. Print:

   "Document prepared successfully."

7. If input_file does not exist:
   - Catch FileNotFoundError.
   - Print:

     "Error: Input document was not found."

Then call the function using:

input file:
"rag_raw_18.txt"

output file:
"rag_processed_18.txt"

Finally, open "rag_processed_18.txt" and print its contents
using .read().
'''

# solution
def prepare_document(input_file , output_file):
    try:
        with open(input_file , "r") as file:
            lines = file.readlines()
        cleaned_lines = ""
        for line in lines:
            if line.strip():
                 cleaned_lines += line
        with open(output_file, "w") as file:
            file.write(cleaned_lines)
        print("Document prepared successfully.")

    except FileNotFoundError:
        print("Error: Input document was not found.")
    
cleaned_lines = prepare_document("rag_raw_18.txt","rag_processed_18.txt")

with open("rag_processed_18.txt", "r") as file:
    contents = file.read()
    print(contents)


