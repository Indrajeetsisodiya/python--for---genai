'''
Exercise 4: Protect API Configuration

Problem:
You have an API configuration stored in a tuple:

api_config = ("gpt-5", 0.7, 1000)

The values represent:

- The model name
- The temperature
- The maximum token limit

Try to change the temperature from `0.7` to `0.9`.

Your goal is to observe what happens when you try to modify a tuple.

Then, create a new tuple called `updated_config` containing:

- "gpt-5"
- 0.9
- 1000

Print `updated_config`.

Expected output:
("gpt-5", 0.9, 1000)
'''

# solution
api_config = ("gpt-5", 0.7, 1000)

# trying to change the temperature from `0.7` to `0.9`
# api_config[1] = 0.9

# throws TypeError: 'tuple' object does not support item assignment since tuples are immuatable 
# print(api_config) 

updated_config = ("gpt-5" , 0.9 , 1000)
print(updated_config)


