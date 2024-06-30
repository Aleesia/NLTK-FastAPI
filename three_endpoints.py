from fastapi import FastAPI, Request
import uvicorn
import nltk

app = FastAPI()

@app.post("/tokenize")
async def tokenize(request: Request):
    data = await request.json()
    text = data.get("text", "")
    result = nltk.tokenize.word_tokenize(text)
    return result


@app.post("/pos_tag")
async def pos_tag(request: Request):
    data = await request.json()
    text = data.get("text", "")
    result = []
    tokenized = nltk.tokenize.sent_tokenize(text)
    for i in tokenized:
        # Word tokenizers is used to find the words and punctuation in a string
        wordsList = nltk.word_tokenize(i) 
	 
	#  Using a part-of-speech tagger 
        tagged = nltk.pos_tag(wordsList)
        result = result + tagged

    return result


@app.post("/ner")
async def ner(request: Request):
    data = await request.json()
    text = data.get("text", "")
    
    result = {} # create dictionary
    for sent in nltk.sent_tokenize(text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                result[' '.join(c[0] for c in chunk)] = chunk.label()
    
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
  
  
