'''
Exercise 4: Use finally with user input

Problem:
Your AI application asks the user to enter the number of
documents to process.

The input must be converted to an integer.

Your task:

1. Use try to perform the conversion.
2. Catch ValueError if the user enters invalid input.
3. If the input is valid, use else to print:

Processing <number> documents...

4. Use finally to ALWAYS print:

Document processing attempt finished.

Test your program with:

10

and:

hello

Observe that the finally message appears in both cases.

# solution
'''

user_input = input("How many documents should be processed? ")

try:
    documents = int(user_input)
except ValueError:
    print("Entered value is invalid")
else:
    print(f"Documents that can be processed: {documents}")

finally:
    print("Document processing attempt finished.")
