'''
Exercise 17: Extract Document Types

Problem:
A document-processing system stores information as tuples:

(document_name, file_type)

Use this data:

documents = [
    ("python.pdf", "pdf"),
    ("rag_notes.txt", "txt"),
    ("llm_guide.pdf", "pdf"),
    ("api_reference.md", "md"),
    ("prompt_guide.txt", "txt"),
    ("vector_db.pdf", "pdf")
]

Create a function called `get_document_types`.

The function should:

1. Receive `documents`.
2. Loop through the list using tuple unpacking.
3. Extract the file type from each tuple.
4. Store the file types in a new list.
5. Return the list.

Call the function and print the result.

Expected output:
['pdf', 'txt', 'pdf', 'md', 'txt', 'pdf']

Do not use a set yet. We will use sets later to remove duplicates.
'''

# solution
documents = [
    ("python.pdf", "pdf"),
    ("rag_notes.txt", "txt"),
    ("llm_guide.pdf", "pdf"),
    ("api_reference.md", "md"),
    ("prompt_guide.txt", "txt"),
    ("vector_db.pdf", "pdf")
]
def get_document_types(documents):
    new_list = []
    for document_name , file_type in documents:
        new_list.append(file_type)
    return new_list

print(get_document_types(documents))
