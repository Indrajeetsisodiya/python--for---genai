'''
Build a function called prepare_rag_documents(filenames, output_file).

The function should:

1. Create an empty string called combined_text.

2. Loop through every filename in filenames.

3. For each file:
   - Try to open it using with open().
   - Read all lines using .readlines().
   - Remove empty/whitespace-only lines.
   - Remove lines beginning with "IGNORE:".
   - Remove lines beginning with "TODO:".
   - Add the remaining lines to combined_text.
   - Add a newline between documents.

4. If a file does not exist:
   - Catch FileNotFoundError.
   - Print:
     "Warning: A document was not found."

5. After processing all files:
   - Write combined_text into output_file.

6. Print:
   "RAG documents prepared successfully."

Then call the function using:

[
    "user_doc_20_a.txt",
    "user_doc_20_b.txt"
]

and create:

"final_rag_documents_20.txt"

Finally:

7. Open "final_rag_documents_20.txt".
8. Read it using .read().
9. Print the final cleaned document.

The final document should contain ONLY useful information.
'''

# solution
def prepare_rag_documents(filenames, output_file):

    combined_text = ""

    for name in filenames:
        try:
            with open(name, "r") as file:
                lines = file.readlines()
                for line in lines:
                     if line.strip():
                        if not line.startswith("IGNORE:") and not line.startswith("TODO:"):
                            combined_text += line 
                combined_text += "\n\n"




        except FileNotFoundError:
             print("Warning: A document was not found.")

    print(repr(combined_text))
    with open(output_file , "w") as file:
         file.write(combined_text)
         print("RAG documents prepared successfully.")

prepare_rag_documents([
    "user_doc_20_a.txt",
    "user_doc_20_b.txt"
],"final_rag_documents_20.txt")


with open("final_rag_documents_20.txt" , "r") as file:
     contents = file.read()
     print(contents)


    
        

            
