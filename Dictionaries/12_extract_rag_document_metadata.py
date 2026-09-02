'''
Exercise 12: Extract RAG Document Metadata

Problem:
Your RAG application retrieves a document chunk:

document = {
    "text": "Python dictionaries store information using key-value pairs.",
    "metadata": {
        "source": "python_guide.pdf",
        "page": 15,
        "chunk_id": "chunk_07",
        "topic": "dictionaries"
    }
}

Extract and print:

1. The document text
2. The source file
3. The page number
4. The topic

Expected Output:
Python dictionaries store information using key-value pairs.
python_guide.pdf
15
dictionaries
'''

# solution
document = {
    "text": "Python dictionaries store information using key-value pairs.",
    "metadata": {
        "source": "python_guide.pdf",
        "page": 15,
        "chunk_id": "chunk_07",
        "topic": "dictionaries"
    }
}

print(document["text"])
print(document["metadata"]["source"])
print(document["metadata"]["page"])
print(document["metadata"]["topic"])