'''
Exercise 10: Prepare Documents for RAG

Problem:
You are preparing documents before sending them to a RAG application.

The documents come from different sources. Each document is stored as a
nested list containing:

[
document_name,
chunk_1,
chunk_2,
...
]

Create a function called prepare_documents_for_rag that:

* Accepts a nested list of documents.
* Extracts all document chunks.
* Ignores the document name, which is always the first item of each document.
* Removes empty chunks.
* Removes chunks containing only spaces.
* Removes chunks that start with "ERROR:".
* Removes duplicate chunks while preserving the first occurrence.
* Returns one flat list of cleaned document chunks.

Example:

documents = [
[
"python_basics.txt",
"Python uses indentation",
"",
"Functions allow code reuse"
],
[
"rag_intro.txt",
"RAG retrieves relevant information",
"Functions allow code reuse",
"   "
],
[
"api_notes.txt",
"APIs allow applications to communicate",
"ERROR: Failed to extract this chunk"
]
]

Output:

[
"Python uses indentation",
"Functions allow code reuse",
"RAG retrieves relevant information",
"APIs allow applications to communicate"
]
'''

# solution
documents = [
[
"python_basics.txt",
"Python uses indentation",
"",
"Functions allow code reuse"
],
[
"rag_intro.txt",
"RAG retrieves relevant information",
"Functions allow code reuse",
"   "
],
[
"api_notes.txt",
"APIs allow applications to communicate",
"ERROR: Failed to extract this chunk"
]
]

def prepare_documents_for_rag(documents):
    cleaned_document = []

    for i in documents:
        for j in i[1:]:
            if j.strip() and not j.startswith("ERROR"):
                if j not in cleaned_document:
                    cleaned_document.append(j)

    return cleaned_document

print(prepare_documents_for_rag(documents))
