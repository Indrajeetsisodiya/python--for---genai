'''
Exercise 5: Find Common Tags

Problem:
Two documents have these tags:

document_a = {"python", "rag", "llm", "api"}
document_b = {"rag", "llm", "vector-db", "api"}

Find the tags that are present in BOTH documents.

Store the result in a set called `common_tags`.

Print `common_tags`.

Expected output:
{'rag', 'llm', 'api'}

The order does not matter.

Requirements:
- Use set intersection.
'''

# solution
document_a = {"python", "rag", "llm", "api"}
document_b = {"rag", "llm", "vector-db", "api"}

common_tags = document_a.intersection(document_b)
print(common_tags)

