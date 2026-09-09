'''
Exercise 3: Check Supported LLM Features

Problem:
An LLM application supports these features:

supported_features = {
    "text",
    "image",
    "json",
    "function_calling"
}

Check whether the following features are supported:

1. "json"
2. "audio"
3. "text"

Print the result of each check.

Expected output:

True
False
True

Requirements:
- Use the `in` operator.
- Do not use a loop.
'''

# solution
supported_features = {
    "text",
    "image",
    "json",
    "function_calling"
}

print("json" in supported_features)
print("audio" in supported_features)
print("text" in supported_features)
