'''
Exercise 5: Clean Document Chunks for RAG

Problem:
You are preparing document chunks before sending them to a RAG system.

The chunks come from different documents and are stored in a nested list.
Each inner list contains:

[
    document_name,
    chunk_text
]

Some chunks should be removed.

Create a function called clean_document_chunks that:

- Accepts a nested list of document chunks.
- Removes chunks with empty text.
- Removes chunks containing only spaces.
- Removes chunks where the text starts with "ERROR:".
- Removes duplicate chunk texts while preserving the first occurrence.
- Returns a new nested list containing the valid chunks.

Important:
When checking for duplicates, compare only the chunk_text.
Do not remove a chunk just because the document_name is the same.

Example:

document_chunks = [
    ["python_basics.txt", "Python uses indentation to define code blocks"],
    ["api_guide.txt", ""],
    ["rag_intro.txt", "RAG retrieves relevant information before generation"],
    ["python_basics.txt", "Python uses indentation to define code blocks"],
    ["error_log.txt", "ERROR: Document could not be processed"],
    ["functions.txt", "Functions allow code to be reused"],
    ["empty.txt", "   "],
    ["backup.txt", "Functions allow code to be reused"]
]

Output:

[
    ["python_basics.txt", "Python uses indentation to define code blocks"],
    ["rag_intro.txt", "RAG retrieves relevant information before generation"],
    ["functions.txt", "Functions allow code to be reused"]
]
'''

# solution
document_chunks = [
    ["python_basics.txt", "Python uses indentation to define code blocks"],
    ["api_guide.txt", ""],
    ["rag_intro.txt", "RAG retrieves relevant information before generation"],
    ["python_basics.txt", "Python uses indentation to define code blocks"],
    ["error_log.txt", "ERROR: Document could not be processed"],
    ["functions.txt", "Functions allow code to be reused"],
    ["empty.txt", "   "],
    ["backup.txt", "Functions allow code to be reused"]
]
def clean_document_chunks(document_chunks):
    cleaned_document_chunks_list = []
    seen_chunks = []


    for i in document_chunks:
        if i[1].strip() and not i[1].startswith("ERROR:"):
            if i[1] not in seen_chunks:
                cleaned_document_chunks_list.append(i)
                seen_chunks.append(i[1])

    return cleaned_document_chunks_list


print(clean_document_chunks(document_chunks))
