'''
Exercise 7: Find Missing Tags

Problem:
Your application supports these tags:

supported_tags = {
    "python",
    "rag",
    "llm",
    "api",
    "vector-db"
}

A document currently has these tags:

document_tags = {
    "python",
    "rag",
    "llm"
}

Find which supported tags are NOT currently used by the document.

Store the result in a set called `missing_tags`.

Print `missing_tags`.

Expected output:
{
    "api",
    "vector-db"
}

The order does not matter.

Requirements:
- Use set difference.
'''

# solution
supported_tags = {
    "python",
    "rag",
    "llm",
    "api",
    "vector-db"
}

document_tags = {
    "python",
    "rag",
    "llm"
}

missing_tags = supported_tags.difference(document_tags)
print(missing_tags)
