# NLTK-FastAPI
REST API that can perform text tokenization, part-of-speech tagging, and named entity recognition.

### 1. Create a virtual environment.

`python3 -m venv env2`

`source env2/bin/activate`

### 2. Install required packages

'pip install nltk fastapi uvicorn'

### 3. Run the application

`uvicorn three_endpoints:app --reload`

Endpoints:

All endpoints take as a parameter JSON with text field.

*/tokenize* - tokenize the given text, returns an array of tokens;

*/pos_tag* - part-of-speech tagging, returns a JSON with pairs (token, tag);

*/ner* - Named Entity Recognition - returns a JSON with array of entities and their types.

 ### 4. Test the application
 
 To test the application, run the file three_endp_check.py:
 
 `python3 three_endp_check.py`
