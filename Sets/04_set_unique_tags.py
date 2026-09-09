'''
Exercise 4: Find Unique Tags

Problem:
You are processing tags from several documents.

document_tags = [
    ["python", "rag", "llm"],
    ["rag", "api", "python"],
    ["llm", "vector-db", "rag"],
    ["api", "python", "prompt"]
]

Create a set called `unique_tags` that contains every unique tag
used across all documents.

Then print the set.

Expected output:
The set should contain:

python
rag
llm
api
vector-db
prompt

The order does not matter.

Requirements:
- Use a set.
- Use a loop.
- Do not manually type the final set of tags.
'''

# solution
document_tags = [
    ["python", "rag", "llm"],
    ["rag", "api", "python"],
    ["llm", "vector-db", "rag"],
    ["api", "python", "prompt"]
]

unique_tags = set()

for tags in document_tags:
    for tag in tags:
        unique_tags.add(tag)

print(unique_tags)



