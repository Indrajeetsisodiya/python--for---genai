'''
Exercise 2: Combine Prompt Sources Without Duplicate Prompts

Problem:
You are building an AI application that receives prompts from three
different sources:

- saved_prompts
- user_prompts
- api_prompts

Create a function called combine_prompt_sources that:

- Accepts three lists of prompts.
- Combines all three lists into one list.
- Removes duplicate prompts.
- Preserves the order in which prompts first appear.
- Returns the final cleaned list.

The order of sources matters:

1. saved_prompts
2. user_prompts
3. api_prompts

Example:

saved_prompts = [
    "Explain Python lists",
    "What is an API?",
    "How does RAG work?"
]

user_prompts = [
    "What is an API?",
    "Explain LLMs"
]

api_prompts = [
    "How does RAG work?",
    "Explain embeddings",
    "Explain LLMs"
]

Output:

[
    "Explain Python lists",
    "What is an API?",
    "How does RAG work?",
    "Explain LLMs",
    "Explain embeddings"
]
'''

# solution 
saved_prompts = [
    "Explain Python lists",
    "What is an API?",
    "How does RAG work?"
]

user_prompts = [
    "What is an API?",
    "Explain LLMs"
]

api_prompts = [
    "How does RAG work?",
    "Explain embeddings",
    "Explain LLMs"
]
combined_prompts = saved_prompts + user_prompts + api_prompts

def combine_prompt_sources(saved_prompts,user_prompts,api_prompts):
    non_redundant_combined_prompts = []

    for prompt in combined_prompts:
        if prompt not in non_redundant_combined_prompts:
            non_redundant_combined_prompts.append(prompt)

    return non_redundant_combined_prompts

print(combine_prompt_sources(saved_prompts , user_prompts , api_prompts))
