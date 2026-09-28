'''
An AI application has generated this response:

"Python file handling is useful for processing documents
before sending their content to an LLM."

Your task:

1. Open "processed_response.txt" in write mode.
2. Save the AI response using .write().
3. Close the file.

4. Open the same file in read mode.
5. Read the complete response using .read().
6. Print the response.
7. Close the file.

Your program should therefore:
- Save the response.
- Read the saved response.
- Print it.
'''

# solution
ai_response = "Python file handling is useful for processing documents before sending their content to an LLM."
f = open("processed_response.txt", "w")
f.write(ai_response)
f.close()

f = open("processed_response.txt" , "r")
text = f.read()
print(text)
f.close()


