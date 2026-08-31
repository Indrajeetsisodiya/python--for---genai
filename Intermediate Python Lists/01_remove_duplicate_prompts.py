'''
Exercise 1: Remove Duplicate Prompts While Preserving Order

Problem:
You are building a simple prompt processing system.

The system receives a list of prompts, but some prompts appear more than once.
Create a function called remove_duplicate_prompts that:

- Accepts a list of prompts.
- Removes duplicate prompts.
- Preserves the original order of the first occurrence.
- Returns the cleaned list.

Important:
Do not use set() directly to create the final result because the order
of the original list must be preserved.

Example:

prompts = [
    "Explain Python functions",
    "What is an API?",
    "Explain Python functions",
    "How does RAG work?",
    "What is an API?",
    "Write a Python function"
]

Output:

[
    "Explain Python functions",
    "What is an API?",
    "How does RAG work?",
    "Write a Python function"
]
'''
# solution 

def remove_duplicate_prompts(prompts):
    non_redundant_prompts = []

    for prompt in prompts:
        if prompt not in non_redundant_prompts:
            non_redundant_prompts.append(prompt)

    return non_redundant_prompts

print(remove_duplicate_prompts([
      "Explain Python functions",
    "What is an API?",
    "Explain Python functions",
    "How does RAG work?",
    "What is an API?",
    "Write a Python function"  
]))

