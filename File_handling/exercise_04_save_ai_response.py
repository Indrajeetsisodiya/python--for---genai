'''
You received a response from an AI model:

"RAG stands for Retrieval-Augmented Generation. It allows an AI system
to retrieve relevant information from external documents before
generating an answer."

Your task:

1. Open a file called "ai_response.txt" in write mode.
2. Save the AI response into the file using .write().
3. Close the file.
4. Print a message saying:
   "AI response saved successfully."

Do not use with open() yet.
'''

# solution
f = open("ai_response.txt", "w")
f.write("RAG stands for Retrieval-Augmented Generation. It allows an AI system to retrieve relevant information from external documents before generating an answer")
f.close()
print("AI response saved successfully.")