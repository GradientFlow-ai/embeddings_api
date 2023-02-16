from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

from embeddings.types import Text

from embeddings.index import create_collection

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello from the embeddings service, we are cooking now!"}

@app.put("/embed_text")
async def json_document(text: Text):

    return {"message": "we got your document", "data": text}


if __name__ == "__main__":
    uvicorn.run("index:app", host='0.0.0.0', port=8000, reload=True)
