'''
Exercise 17: Create a custom exception for RAG documents

Problem:
Your RAG pipeline should reject documents that contain
fewer than 100 characters.

Your task:

1. Create a custom exception called:

DocumentTooShortError

2. It should inherit from Exception.

3. Ask the user to enter a document.

4. If the document contains fewer than 100 characters,
   raise DocumentTooShortError with this message:

"Document is too short for RAG processing."

5. Catch DocumentTooShortError using "as error".

6. Print the actual error message.

7. If the document is long enough, use else to print:

"Document accepted for RAG processing."

8. Always use finally to print:

"Document validation finished."

Test your program with:
- a short sentence
- a document containing 100+ characters

Hint:
Use len() to determine the number of characters.

# solution
'''
class DocumentTooShortError(Exception):
    pass

user_input = (input("Enter the document: "))
try:
    if len(user_input ) < 100:
        raise DocumentTooShortError("Document is too short for RAG processing.")
except DocumentTooShortError as error:
    print(error)
else:
    print("Document accepted for RAG processing.")
finally:
    print("Document Validation finished.")


        




