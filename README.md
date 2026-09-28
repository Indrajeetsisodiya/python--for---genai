# Python for GenAI

Python fundamentals, practical coding exercises, and projects for my journey toward becoming a GenAI Developer / AI Application Developer.

## Completed Topics

* Loops
* Functions
* Intermediate Python Lists
* Python Dictionaries
* Python Tuples
* Python Sets
* Python Exception Handling
* Python File Handling
* JSON
* Modules and Imports
* Virtual Environments and pip

---

## Loop Exercises Covered

* `enumerate()`
* Counting items
* Filtering prompts
* Counting words
* Finding longest responses
* Finding max/min values
* String transformations
* List transformations

---

## Function Exercises Covered

### Level 1: Counting Functions — 15 Exercises

* Count messages
* Count long messages
* Count questions
* Count AI mentions
* Count short messages
* Count Python mentions
* Count empty messages
* Count messages with exclamation marks
* Count messages starting with AI
* Count messages containing numbers
* Count messages with more than three words
* Count messages containing Python or AI
* Count messages containing both Python and AI
* Count messages with exactly three words
* Count messages containing GenAI

### Level 2: Filtering Functions — 10 Exercises

* Get long messages
* Get questions
* Get Python messages
* Get messages with numbers
* Get messages with more than three words
* Get messages containing Python or AI
* Get messages containing both Python and AI
* Get short messages
* Get messages starting with AI
* Get messages ending with exclamation marks

---

## Intermediate Python Lists

### Practical List Processing for GenAI — 15 Exercises

* Removing duplicates while preserving order
* Combining multiple prompt sources
* Extracting user messages from structured chat data
* Cleaning API responses
* Cleaning document chunks
* Flattening nested document chunks
* Finding the longest valid document chunk
* Finding the shortest valid document chunk
* Combining and cleaning multiple document sources
* Preparing document chunks for RAG
* Extracting successful API documents
* Extracting and cleaning nested API document chunks
* Selecting useful document chunks based on quality rules
* Preparing high-quality chunks for a RAG pipeline
* Building a final RAG context with cleaned, longest, and shortest chunks

### Concepts Practiced

* Combining lists
* Removing duplicates while preserving order
* Extracting useful data from lists
* Removing unwanted items
* Working with nested lists
* Flattening nested lists
* Cleaning API-like responses
* Processing document chunks
* Filtering API responses
* Finding longest and shortest values
* Preparing cleaned data for RAG applications

---

## Python Dictionaries

### Practical Dictionary Processing for GenAI — 15 Exercises

* Creating and accessing dictionaries
* Updating dictionary values
* Adding new key-value pairs
* Removing unwanted dictionary data
* Checking whether a key exists
* Looping through dictionaries
* Accessing nested dictionaries
* Processing lists of dictionaries
* Extracting user messages from chat data
* Extracting data from API responses
* Processing LLM responses
* Working with RAG document metadata
* Filtering RAG document chunks
* Processing JSON-like API responses
* Filtering RAG search results using similarity scores

### Concepts Practiced

* Key-value pairs
* Dictionary access
* Dictionary updates
* Adding and removing data
* Checking dictionary keys
* `.items()`
* `.get()`
* `.update()`
* `.pop()`
* Nested dictionaries
* Lists of dictionaries
* Filtering structured data
* Processing API-like responses
* Processing LLM responses
* Working with document metadata
* Preparing and filtering RAG search results

---

## Python Tuples

### Practical Tuple Processing for GenAI — 21 Exercises

* Accessing tuple elements
* Tuple unpacking
* Working with tuples in loops
* Understanding tuple immutability
* Processing API configuration data
* Processing LLM API responses
* Working with lists of tuples
* Filtering RAG search results
* Returning tuples from functions
* Processing document metadata
* Filtering documents using tuple data
* Extracting user questions from chat messages
* Processing API status responses
* Finding the highest similarity score
* Returning the best RAG result
* Counting successful API responses
* Extracting document file types
* Grouping RAG results
* Working with nested tuples
* Processing chat messages stored as tuples
* Creating updated tuples from existing data

### Concepts Practiced

* Tuple creation
* Indexing
* Tuple unpacking
* Iterating through tuples
* Tuple immutability
* Lists of tuples
* Nested tuples
* Returning multiple values from functions
* Processing structured API data
* Processing RAG results
* Working with chat message data

---

## Python Sets

### Practical Set Processing for GenAI — 20 Exercises

* Removing duplicate document IDs
* Adding and removing tags
* Checking supported features
* Finding unique tags
* Finding common document tags
* Combining document tags
* Finding missing tags
* Comparing application and model features
* Checking user permissions
* Finding missing permissions
* Combining search results
* Finding common documents
* Finding documents unique to one search method
* Comparing retrieval results
* Removing duplicate document tags
* Finding unsupported model features
* Checking required document tags
* Finding extra permissions
* Comparing RAG retrieval results
* Performing a final RAG document analysis

### Concepts Practiced

* Creating sets
* Removing duplicates
* Membership checking with `in`
* `.add()`
* `.update()`
* `.remove()`
* `.intersection()`
* `.union()`
* `.difference()`
* `.issubset()`
* Comparing collections
* Working with unique document IDs
* Processing permissions
* Processing tags
* Comparing RAG retrieval results

---

## Python Exception Handling

### Practical Exception Handling for GenAI — 20 Exercises

* Handling invalid user input
* Handling `ValueError`
* Handling missing dictionary keys with `KeyError`
* Handling multiple exception types
* Using `else` with exception handling
* Using `finally`
* Handling `TypeError`
* Handling errors in API-like responses
* Understanding exception scope
* Using `raise` for validation
* Using `as error` to access exception messages
* Handling `FileNotFoundError`
* Handling `PermissionError`
* Understanding specific vs generic exceptions
* Handling `AttributeError` in LLM-style responses
* Handling API connection errors
* Handling API timeout errors
* Creating custom exceptions
* Handling invalid JSON with `JSONDecodeError`
* Validating AI API responses

### Concepts Practiced

* `try`
* `except`
* Multiple `except` blocks
* `else`
* `finally`
* `raise`
* `as error`
* `ValueError`
* `KeyError`
* `TypeError`
* `ZeroDivisionError`
* `FileNotFoundError`
* `PermissionError`
* `ConnectionError`
* `TimeoutError`
* `AttributeError`
* Custom exceptions
* `JSONDecodeError`
* Safe API/LLM response handling
* Input validation
* Error handling in GenAI applications

---

## Python File Handling

### Practical File Handling for GenAI — 20 Exercises

* Opening and reading text files
* Reading files with `.read()`
* Reading files line by line with `.readline()`
* Reading multiple lines with `.readlines()`
* Understanding file modes
* Writing AI responses to files
* Appending AI logs
* Saving and reading generated AI responses
* Cleaning documents by removing empty lines
* Using `with open()` for safe file handling
* Handling missing files with `FileNotFoundError`
* Handling file permission errors with `PermissionError`
* Safely processing user-uploaded documents
* Cleaning raw RAG documents
* Filtering `IGNORE:` and `TODO:` lines
* Creating reusable document-cleaning functions
* Handling missing documents inside functions
* Preparing processed documents
* Combining multiple documents
* Building a final RAG-style document preprocessing workflow

### Concepts Practiced

* `open()`
* File modes: `"r"`, `"w"`, `"a"`
* `.read()`
* `.readline()`
* `.readlines()`
* `.write()`
* `with open()`
* `\n` and `\n\n`
* `.strip()`
* `.startswith()`
* File path handling
* `FileNotFoundError`
* `PermissionError`
* Reading and writing text
* Cleaning document content
* Processing multiple documents
* Building reusable file-processing functions
* Preparing documents for RAG pipelines

---

## JSON

### Concepts Practiced

* Reading JSON data
* Writing JSON data
* Converting JSON to Python objects
* Converting Python objects to JSON
* Working with JSON-like API responses
* Processing structured AI data
* Handling invalid JSON

---

## Modules and Imports

### Concepts Practiced

* Creating Python modules
* Importing modules
* Using functions from other files
* Organizing Python code
* Reusing code across projects
* Understanding basic project structure

---

## Virtual Environments and pip

### Concepts Practiced

* Creating virtual environments
* Activating virtual environments
* Installing packages with `pip`
* Managing project dependencies
* Understanding isolated Python environments
* Preparing projects for real-world development

---

## Upcoming Topics

* APIs and HTTP Requests
* `requests` / `httpx`
* API Authentication
* API Error Handling
* Pydantic and Data Validation
* FastAPI
* LLM Applications
* RAG
* Embeddings
* Vector Databases
* AI Agents

---

## Goal

Build strong Python fundamentals and practical development skills for becoming a GenAI Developer / AI Application Developer.

The focus is on practical development with:

* APIs
* LLM applications
* RAG pipelines
* Embeddings
* Vector databases
* AI agents
* Real-world AI applications
