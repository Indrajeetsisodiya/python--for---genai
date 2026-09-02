'''
Exercise 6: Loop Through Document Metadata

Problem:
You have metadata for a document chunk:

metadata = {
    "source": "python_guide.pdf",
    "page": 12,
    "topic": "dictionaries",
    "chunk_id": "chunk_04"
}

Use a loop to print each key and its value.

Expected Output:
source : python_guide.pdf
page : 12
topic : dictionaries
chunk_id : chunk_04
'''

# solution
metadata = {
    "source": "python_guide.pdf",
    "page": 12,
    "topic": "dictionaries",
    "chunk_id": "chunk_04"
}

for key, value in metadata.items():
    print(key,":",value)
