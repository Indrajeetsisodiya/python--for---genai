'''
Exercise 5: Check Whether an API Response Contains a Key

Problem:
You receive this API-like response:

response = {
    "status": "success",
    "answer": "RAG combines retrieval with generation.",
    "model": "gpt-5"
}

Check whether the dictionary contains the key "answer".

If it exists, print:

Answer found

Otherwise, print:

Answer not found

Expected Output:
Answer found
'''

# solution
response = {
    "status": "success",
    "answer": "RAG combines retrieval with generation.",
    "model": "gpt-5"
}
if "answer" in response:
    print("Answer found")
else:
    print("Answer not found")



