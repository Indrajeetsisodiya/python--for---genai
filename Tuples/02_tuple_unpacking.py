'''
Exercise 2: Unpack an API Result

Problem:
An LLM API returns the following tuple:

api_result = ("success", 256)

Use tuple unpacking to store the two values in separate variables:

- `status`
- `tokens`

Then print both variables.

Do NOT access the values using indexing such as api_result[0] or api_result[1].

Example:
api_result = ("success", 256)

Output:
success
256
'''

# solution
api_result = ("success", 256)
status , tokens = api_result # tuple unpacking 
print(status)
print(tokens)
