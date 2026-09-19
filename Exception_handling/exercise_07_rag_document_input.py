'''
Exercise 7: Handle invalid document input

Problem:
A simple RAG-style application asks the user how many
documents should be retrieved.

The user must enter a whole number.

The program should:

1. Ask the user for the number.
2. Convert the input to an integer.
3. If the conversion fails, print:

Invalid document count.

4. If successful, use else to print:

Retrieving <number> documents...

5. Always use finally to print:

Retrieval attempt finished.

Important:
Keep the try block focused only on the operation
that can raise ValueError.

# solution
'''

user_input = input("How many documents should be retrieved? ")

# solution
try:
    number = int(user_input)
except ValueError:
    print("Invalid document count.")
else:
    print(f"Retrieving {number} documents...")

finally:
    print("Retrieval attempt finished.")

