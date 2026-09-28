'''
You have two documents:

"document_19_a.txt"
"document_19_b.txt"

Create a function called combine_documents(filenames, output_file).

The function should:

1. Create an empty string called combined_text.
2. Loop through every filename in the filenames list.
3. Try to open each file using with open().
4. Read its contents using .read().
5. Add the contents to combined_text.
6. Add a newline between documents.
7. If a file is missing, catch FileNotFoundError and print:

   "Error: One of the documents was not found."

8. After processing the files, write combined_text into output_file.

Then call the function using:

[
    "document_19_a.txt",
    "document_19_b.txt"
]

and create:

"combined_rag_documents_19.txt"

Finally, read the combined file and print its contents.

Do not worry about removing duplicate content yet.
'''

# solution
def combine_documents(filenames, output_file):
    combined_text = ""
    for filename in filenames:
        try:
            with open(filename,"r") as file:
                text = file.read()
            combined_text += text
            combined_text += "\n"

        except FileNotFoundError:
            print("Error: One of the documents was not found.")

    with open(output_file, "w") as file:
        file.write(combined_text)

combine_documents(["document_19_a.txt", "document_19_b.txt"], "combined_rag_documents_19.txt" )

with open("combined_rag_documents_19.txt", "r") as file:
    contents = file.read()
    print(contents)








    
    
        