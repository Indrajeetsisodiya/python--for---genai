'''
Exercise 9: Combine and Clean Multiple Document Sources

Problem:
You are preparing documents for a RAG application.

The application receives document chunks from three different sources:

- website_chunks
- pdf_chunks
- user_chunks

Each source is a list of text chunks.

Create a function called combine_clean_document_sources that:

- Accepts the three lists.
- Processes the sources in this order:
  1. website_chunks
  2. pdf_chunks
  3. user_chunks
- Combines all chunks into one list.
- Removes empty chunks.
- Removes chunks containing only spaces.
- Removes chunks that start with "ERROR:".
- Removes duplicate chunks while preserving the first occurrence.
- Returns the final cleaned list.

Example:

website_chunks = [
    "Python is used for AI development",
    "",
    "RAG retrieves relevant information",
    "ERROR: Website could not be processed"
]

pdf_chunks = [
    "Embeddings convert text into vectors",
    "Python is used for AI development",
    "   ",
    "Functions make code reusable"
]

user_chunks = [
    "RAG retrieves relevant information",
    "LLMs generate text based on input",
    "Functions make code reusable"
]

Output:

[
    "Python is used for AI development",
    "RAG retrieves relevant information",
    "Embeddings convert text into vectors",
    "Functions make code reusable",
    "LLMs generate text based on input"
]
'''

# solution
website_chunks = [
    "Python is used for AI development",
    "",
    "RAG retrieves relevant information",
    "ERROR: Website could not be processed"
]

pdf_chunks = [
    "Embeddings convert text into vectors",
    "Python is used for AI development",
    "   ",
    "Functions make code reusable"
]

user_chunks = [
    "RAG retrieves relevant information",
    "LLMs generate text based on input",
    "Functions make code reusable"
]

def combine_clean_document_sources(website_chunks , pdf_chunks , user_chunks):
    cleaned_document = []

    for chunk in website_chunks, pdf_chunks,user_chunks:
        for j in chunk :
            if j.strip() and not j.startswith("ERROR"):
                if j not in cleaned_document:
                    cleaned_document.append(j)

    return cleaned_document

print(combine_clean_document_sources(website_chunks, pdf_chunks,user_chunks))



