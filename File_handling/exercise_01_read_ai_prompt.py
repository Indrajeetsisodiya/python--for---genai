'''
You have a text file called "ai_prompt.txt".

The file contains an AI prompt, for example:

"Explain what RAG is in simple terms."

Your task:

1. Open the file in read mode.
2. Read the complete contents of the file.
3. Print the contents to the screen.
4. Close the file after reading it.

Use:
- open()
- read()
- close()

Do not use with open() yet. We will learn that later.
'''

# solution
file = open("ai_prompt.txt", "r")
text = file.read()
print(text)
file.close()
