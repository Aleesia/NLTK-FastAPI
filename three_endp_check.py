import requests
import json

# Get some random text from Wikipedia to check the application
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': 'Lana Del Rey',
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
    }
).json()
page = next(iter(response['query']['pages'].values()))
text = page['extract'] # take just the extract for our analysis
data = {"text": text}

data = json.dumps(data) # convert the data into JSON format

# URLs for three different endpoints:
url_tokenize = "http://127.0.0.1:8000/tokenize"
url_pos_tag = "http://127.0.0.1:8000/pos_tag"
url_ner = "http://127.0.0.1:8000/ner"

# Send POST requests to http://127.0.0.1:8000/tokenize, .../pos_tag, .../ner
response_tokens = requests.post(url_tokenize, data=data).json()
response_pos_tag = requests.post(url_pos_tag, data=data).json()
response_ner = requests.post(url_ner, data=data).json()

# print the results:
print("response_tokenized: ", response_tokens)
print("response_pos_tag: ", response_pos_tag)
print("response_ner: ", response_ner)

