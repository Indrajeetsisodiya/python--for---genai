'''
You have a file called "ai_log.txt".

Your application needs to record an AI interaction.

The file may already contain previous logs.

Your task:

1. Open "ai_log.txt" in append mode.
2. Add this new log entry:

   "User asked: What is RAG?
   AI responded: RAG retrieves relevant information before generating an answer."

3. Make sure the new entry is added to the END of the file.
4. Close the file.
5. Print:

   "AI interaction logged successfully."

Important:
Do NOT use "w" mode because existing logs must not be deleted.
'''

# solution
f = open("ai_log.txt", "a")
f.write(   "User asked: What is RAG? \nAI responded: RAG retrieves relevant information before generating an answer.")
f.close()
print( "AI interaction logged successfully.")