'''
Exercise 15: Remove Duplicate Tags from Documents

Problem:
You receive tags from several documents in an AI application.

document_1_tags = ["python", "ai", "llm", "python"]
document_2_tags = ["rag", "llm", "python", "rag"]
document_3_tags = ["ai", "agents", "llm"]

Create a set called `unique_tags` containing every unique tag
across all three documents.

Print `unique_tags`.

Expected output:
{'python', 'ai', 'llm', 'rag', 'agents'}

Hint:
You can start with an empty set and add the tags from each
document.
'''

# solution 

document_1_tags = ["python", "ai", "llm", "python"]
document_2_tags = ["rag", "llm", "python", "rag"]
document_3_tags = ["ai", "agents", "llm"]

unique_tags = set(document_1_tags).union(set(document_2_tags)).union(set(document_3_tags))
print(unique_tags)

# another way of doing it ------
unique_tags = set()

unique_tags.update(document_1_tags)
unique_tags.update(document_2_tags)
unique_tags.update(document_3_tags)

print(unique_tags)