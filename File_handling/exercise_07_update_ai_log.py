'''
You have an AI application that stores its responses in "ai_responses.txt".

Your task:

1. Open "ai_responses.txt" in write mode.
2. Write this first AI response:

   "Response 1: RAG helps an AI use external information."

3. Close the file.

4. Open the SAME file again, but this time in append mode.

5. Add this second response:

   "Response 2: Embeddings help represent text as numerical vectors."

6. Close the file.

7. Print:

   "AI responses saved successfully."

The final file should contain BOTH responses.

Important:
Use "w" for the first response and "a" for the second response.
'''

# solution
f = open("ai_responses.txt", "w")
f.write("Response 1: RAG helps an AI use external information.\n")
f.close()

f = open("ai_responses.txt", "a")
f.write("Response 2: Embeddings help represent text as numerical vectors.")
f.close()

print("AI responses saved successfully.")