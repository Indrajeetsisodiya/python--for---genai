'''
Exercise 6: Combine Tags from Two Documents

Problem:
Two documents have these tags:

document_a = {"python", "rag", "llm"}
document_b = {"api", "rag", "vector-db"}

Find ALL unique tags used by either document.

Store the result in a set called `all_tags`.

Print `all_tags`.

Expected output:
The set should contain:

python
rag
llm
api
vector-db

The order does not matter.

Requirements:
- Use set union.
'''

# solution
document_a = {"python", "rag", "llm"}
document_b = {"api", "rag", "vector-db"}


all_tags = document_a.union(document_b)
print(all_tags)
