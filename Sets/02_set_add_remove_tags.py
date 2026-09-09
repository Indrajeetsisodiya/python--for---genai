'''
Exercise 2: Update Document Tags

Problem:
A document currently has these tags:

tags = {"python", "rag", "llm"}

Perform the following operations:

1. Add the tag `"api"` to the set.
2. Remove the tag `"llm"` from the set.
3. Print the final set.

Expected output:
The set should contain:

{"python", "rag", "api"}

The order does not matter.

Requirements:
- Use `.add()` to add the new tag.
- Use `.remove()` to remove the old tag.
'''

# solution
tags = {"python", "rag", "llm"}
tags.add("api")
tags.remove("llm")
print(tags)

