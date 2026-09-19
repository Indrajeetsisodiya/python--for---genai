'''
Exercise 9: Display the actual exception message

Problem:
Your RAG application validates a document count.

The document count must:
- Be an integer
- Not be negative
- Not be greater than 100

Your task:

1. Get the user's input.
2. Convert it to an integer.
3. If the number is negative, raise:

ValueError("Document count cannot be negative.")

4. If the number is greater than 100, raise:

ValueError("Document count cannot be greater than 100.")

5. Catch ValueError using "as error".
6. Print the actual exception message using the error variable.
7. If there is no exception, use else to print:

Retrieving <number> documents...

8. Always use finally to print:

Document retrieval attempt finished.

Test with:

10
-5
150
hello

# solution
'''
user_input = input("enter the document count ")

try:
    number = int(user_input)
    if number > 100:
        raise ValueError("document count can not be greater than 100")
    if number < 0:
        raise ValueError("document count can not be negative")
    
except ValueError as error:
    print(error)
else:
    print(f"Retrieving {number} documents...")
finally:
    print("Document retrieval attempt finished.")
