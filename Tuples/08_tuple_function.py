'''
Exercise 8: Return Multiple Values from an LLM Function

Problem:
Create a function called `process_llm_response` that receives:

- `response` — a string containing an LLM response
- `tokens` — an integer representing the number of tokens used

The function should return both values together as a tuple.

Then call the function with:

response = "RAG retrieves relevant documents"
tokens = 142

Store the returned tuple in a variable called `result`.

Use tuple unpacking to store the returned values in:

- `llm_response`
- `token_count`

Finally, print both values.

Expected output:
RAG retrieves relevant documents
142
'''

# solution
def process_llm_response (response, tokens):
    return response, tokens

llm_response, token_count = process_llm_response("RAG retrieves relevant documents",142)

print(llm_response)
print(token_count)


