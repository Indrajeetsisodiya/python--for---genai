'''
Exercise 19: Process Nested API Data

Problem:
An API returns information about an LLM model as a tuple:

model_data = (
    "gpt-5",
    ("text", "image"),
    128000
)

The values represent:

- Model name
- Supported input types
- Maximum context length

Use tuple unpacking to extract:

- `model_name`
- `supported_inputs`
- `context_length`

Then:

1. Print the model name.
2. Loop through `supported_inputs` and print each supported input type.
3. Print the context length.

Expected output:

gpt-5
text
image
128000

Requirements:
- Use tuple unpacking.
- Use a `for` loop.
- Do not use indexing such as `model_data[0]`.
'''
# solution
model_data = (
    "gpt-5",
    ("text", "image"),
    128000
)

model_name, supported_inputs, context_length = model_data

print(model_name)

for input_type in supported_inputs:
    print(input_type)

print(context_length)
