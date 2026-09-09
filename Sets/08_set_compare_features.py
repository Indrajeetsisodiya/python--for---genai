'''
Exercise 8: Compare LLM Features

Problem:
Your application supports these features:

app_features = {
    "text",
    "image",
    "json",
    "function_calling"
}

A particular model supports:

model_features = {
    "text",
    "image",
    "json"
}

Find:

1. Features supported by BOTH the application and the model.
2. Features supported by the application but NOT by the model.

Store them in:

- `supported_by_both`
- `not_supported_by_model`

Print both sets.

Expected output:

Supported by both:
{'text', 'image', 'json'}

Not supported by model:
{'function_calling'}

The order does not matter.

Requirements:
- Use set intersection for the first result.
- Use set difference for the second result.
'''

# solution
app_features = {
    "text",
    "image",
    "json",
    "function_calling"
}

model_features = {
    "text",
    "image",
    "json"
}

supported_by_both = app_features.intersection(model_features)
not_supported_by_model = app_features.difference(model_features)

print(supported_by_both)
print(not_supported_by_model)
