'''
Exercise 17: Check Whether a Document Has All Required Tags

Problem:
An AI application requires every document used for a specific
RAG workflow to have these tags:

required_tags = {
    "python",
    "ai",
    "tutorial"
}

A document has these tags:

document_tags = {
    "python",
    "ai",
    "tutorial",
    "beginner"
}

Check whether the document contains ALL the required tags.

Store the Boolean result in `is_valid`.

Print `is_valid`.

Expected output:
True

Hint:
Think about the set method that checks whether one set
is completely contained inside another set.
'''

# solution
required_tags = {
    "python",
    "ai",
    "tutorial"
}

document_tags = {
    "python",
    "ai",
    "tutorial",
    "beginner"
}

is_valid = required_tags.issubset(document_tags)
print(is_valid)
