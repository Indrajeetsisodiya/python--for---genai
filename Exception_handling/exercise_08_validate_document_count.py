'''
Exercise 8: Raise an exception for invalid document counts

Problem:
Your RAG application should never retrieve a negative
number of documents.

The user enters a document count.

Your task:

1. Convert the user's input to an integer.
2. If the number is negative, use raise to raise:

ValueError("Document count cannot be negative.")

3. Catch the ValueError.
4. Print the error message when a ValueError occurs.
5. If everything is valid, use else to print:

Retrieving <number> documents...

6. Always use finally to print:

Document retrieval attempt finished.

Test your program with:

5

-3

hello

Hint:
There are now TWO ways ValueError can happen:
- Python raises it when int() receives invalid text.
- You raise it yourself when the number is negative.

# solution
'''

user_input = input("How many documents should be retrieved? ")
try:
    number = int(user_input)
    if number < 0:
        raise ValueError("Document count cannot be negative.")
except ValueError:
    print("Please enter a valid document count")
else:
    print(f"Retrieving {number} documents...")
finally:
    print("Document retrieval attempt finished.")



