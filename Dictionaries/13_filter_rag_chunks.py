'''
Exercise 13: Filter RAG Document Chunks

Problem:
Your RAG system retrieved these document chunks:

documents = [
    {
        "text": "Python dictionaries store data using key-value pairs.",
        "metadata": {
            "source": "python_guide.pdf",
            "topic": "dictionaries"
        }
    },
    {
        "text": "Python lists store multiple values in a sequence.",
        "metadata": {
            "source": "python_guide.pdf",
            "topic": "lists"
        }
    },
    {
        "text": "Dictionaries are commonly used to represent JSON data.",
        "metadata": {
            "source": "api_guide.pdf",
            "topic": "dictionaries"
        }
    }
]

Create an empty list called dictionary_chunks.

Loop through the documents and add the entire document dictionary
to dictionary_chunks only when its topic is "dictionaries".

Finally, print dictionary_chunks.

Expected Output:
[
    {
        "text": "Python dictionaries store data using key-value pairs.",
        "metadata": {
            "source": "python_guide.pdf",
            "topic": "dictionaries"
        }
    },
    {
        "text": "Dictionaries are commonly used to represent JSON data.",
        "metadata": {
            "source": "api_guide.pdf",
            "topic": "dictionaries"
        }
    }
]
'''

# solution
documents = [
    {
        "text": "Python dictionaries store data using key-value pairs.",
        "metadata": {
            "source": "python_guide.pdf",
            "topic": "dictionaries"
        }
    },
    {
        "text": "Python lists store multiple values in a sequence.",
        "metadata": {
            "source": "python_guide.pdf",
            "topic": "lists"
        }
    },
    {
        "text": "Dictionaries are commonly used to represent JSON data.",
        "metadata": {
            "source": "api_guide.pdf",
            "topic": "dictionaries"
        }
    }
]

dictionary_chunks = []

for chunk in documents:
    if chunk["metadata"]["topic"] == "dictionaries":
        dictionary_chunks.append(chunk)

print(dictionary_chunks)