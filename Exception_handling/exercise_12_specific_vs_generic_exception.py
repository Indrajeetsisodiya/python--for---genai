'''
Exercise 12: Catch the correct exception

Problem:
Your AI application receives a document count as text.

The application expects an integer.

Your task:

1. Ask the user for the document count.
2. Convert it to an integer.
3. Handle the expected conversion error specifically.
4. Do NOT use "except Exception".
5. If conversion succeeds, use else to print:

Document count accepted: <number>

6. If conversion fails, print:

Invalid document count.

7. Always use finally to print:

Validation finished.

Important:
This exercise is testing whether you can choose
the SPECIFIC exception instead of catching everything.

# solution
'''
user_input = input("enter documents here: ")
try:
    number = int(user_input)

except ValueError:
    print("Invalid document count.")

else:
    print("Document count accepted:", number)

finally:
    print("Validation finished.")
    