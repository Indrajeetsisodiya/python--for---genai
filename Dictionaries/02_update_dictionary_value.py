'''
Exercise 2: Update an LLM Response

Problem:
You are given a dictionary representing an LLM response:

response = {
    "model": "gpt-5",
    "status": "processing",
    "answer": "Python is a programming language."
}

The response has finished processing.

Update the "status" value from "processing" to "completed".

Then print the updated status.

Expected Output:
completed
'''

# Solution
response = {
    "model": "gpt-5",
    "status": "processing",
    "answer": "Python is a programming language."
}

# one way for updating dict 
# response.update({"status": "completed"})
# print(response.get("status"))

# another way 
response["status"] = "completed"
print(response["status"])

