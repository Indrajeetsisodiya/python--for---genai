'''
Exercise 20: Final Set Challenge — RAG Document Analysis

Problem:
An AI application retrieves documents using two methods.

Vector search found:

vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}

Keyword search found:

keyword_results = {
    "doc_103",
    "doc_104",
    "doc_105",
    "doc_106"
}

The application requires these documents for its final answer:

required_documents = {
    "doc_103",
    "doc_104"
}

Find THREE things:

1. Documents found by BOTH retrieval methods.
   Store in `common_documents`.

2. All unique documents found by either retrieval method.
   Store in `all_documents`.

3. Check whether ALL required documents were retrieved
   by at least one of the two search methods.

   Store the Boolean result in `all_required_found`.

Print all three variables.

Expected output:

common_documents:
{'doc_103', 'doc_104', 'doc_105'}

all_documents:
{'doc_101', 'doc_102', 'doc_103', 'doc_104', 'doc_105', 'doc_106'}

all_required_found:
True

Hint:
You will need:
- one operation for BOTH
- one operation for ALL/EITHER
- one operation to check whether required documents
  are contained inside the retrieved documents
'''

# solution
vector_results = {
    "doc_101",
    "doc_102",
    "doc_103",
    "doc_104",
    "doc_105"
}


keyword_results = {
    "doc_103",
    "doc_104",
    "doc_105",
    "doc_106"
}


required_documents = {
    "doc_103",
    "doc_104"
}

common_documents = vector_results.intersection(keyword_results)
all_documents = vector_results.union(keyword_results)
all_required_found = required_documents.issubset(all_documents)
print(common_documents)
print(all_documents)
print(all_required_found)
