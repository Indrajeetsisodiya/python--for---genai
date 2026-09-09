'''
Exercise 9: Process Document Metadata

Problem:
A document processing system stores metadata as tuples.

Each tuple contains:

(document_name, file_type, page_count)

Use the following data:

documents = [
    ("python.pdf", "pdf", 12),
    ("rag_notes.txt", "txt", 5),
    ("llm_guide.pdf", "pdf", 20),
    ("api_reference.txt", "txt", 8)
]

Use a `for` loop and tuple unpacking.

Print only the documents that:

1. Have the file type `"pdf"`
2. Have more than 10 pages

Expected output:
python.pdf pdf 12
llm_guide.pdf pdf 20
'''

# solution
# (document_name, file_type, page_count)

documents = [
    ("python.pdf", "pdf", 12),
    ("rag_notes.txt", "txt", 5),
    ("llm_guide.pdf", "pdf", 20),
    ("api_reference.txt", "txt", 8)
]

for document_name, file_type, page_count in documents:
    if file_type == "pdf" and page_count > 10:
        print(document_name, file_type, page_count)