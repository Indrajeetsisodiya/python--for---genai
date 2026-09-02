'''
Exercise 15: Filter RAG Search Results

Problem:
A vector search system returns these results:

search_results = [
    {
        "text": "Python dictionaries store data using key-value pairs.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 15
        },
        "score": 0.92
    },
    {
        "text": "Python lists store multiple values in a sequence.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 10
        },
        "score": 0.71
    },
    {
        "text": "Dictionaries are commonly used for JSON data.",
        "metadata": {
            "source": "api_guide.pdf",
            "page": 8
        },
        "score": 0.88
    },
    {
        "text": "Python functions can accept parameters.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 20
        },
        "score": 0.63
    }
]

Create an empty list called relevant_results.

Loop through search_results and add the entire result
to relevant_results only when its score is greater than or equal to 0.85.

Finally, print relevant_results.

Expected Output:
The results with scores:

0.92
0.88

should be included.

The results with scores:

0.71
0.63

should not be included.
'''

# solution
search_results = [
    {
        "text": "Python dictionaries store data using key-value pairs.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 15
        },
        "score": 0.92
    },
    {
        "text": "Python lists store multiple values in a sequence.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 10
        },
        "score": 0.71
    },
    {
        "text": "Dictionaries are commonly used for JSON data.",
        "metadata": {
            "source": "api_guide.pdf",
            "page": 8
        },
        "score": 0.88
    },
    {
        "text": "Python functions can accept parameters.",
        "metadata": {
            "source": "python_guide.pdf",
            "page": 20
        },
        "score": 0.63
    }
]

relevant_results = []

for result in search_results:
    if result["score"] >= 0.85:
        relevant_results.append(result)

print(relevant_results)
