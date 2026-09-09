'''
Exercise 16: Find Missing Features

Problem:
An AI application supports these features:

app_features = {
    "chat",
    "document_search",
    "summarization",
    "image_analysis",
    "web_search"
}

A particular AI model supports:

model_features = {
    "chat",
    "document_search",
    "summarization"
}

Find the features that the application supports but the model
does NOT support.

Store the result in `unsupported_features`.

Print `unsupported_features`.

Expected output:
{'image_analysis', 'web_search'}

Hint:
Think about `difference()`.
'''

# solution
app_features = {
    "chat",
    "document_search",
    "summarization",
    "image_analysis",
    "web_search"
}
model_features = {
    "chat",
    "document_search",
    "summarization"
}

unsupported_features = app_features.difference(model_features)
print(unsupported_features)
