from embeddings.types import Text
import hashlib
from chromadb.utils import embedding_functions

from chroma_client import chroma_client

EmbeddingFunctions = {
    "default": embedding_functions.SentenceTransformerEmbeddingFunction,
    "openAI": embedding_functions.OpenAIEmbeddingFunction
    }


def create_collection(username: str, embedding_function: str = "default"):
    collection_name = hashlib.sha256(username.encode()).hexdigest()
    print(name)
    emb_fn = EmbeddingFunctions[embedding_function]
    collection = client.create_collection(name=collection_name, embedding_function=emb_fn, metric="dot", dimension=768)

    # TODO send to DB service
    return collection


def embed_text(text: Text, username: str):
    collection_name = hashlib.sha256(username.encode()).hexdigest()
    collection = client.get_collection(name=collection_name)

    document_id = hashlib.sha256(text.encode()).hexdigest()

    collection.add_document(
        documents=[text],
        ids=[document_id]
    )

def get_similar_texts(text: Text, username: str):
    collection_name = hashlib.sha256(username.encode()).hexdigest()
    collection = client.get_collection(name=collection_name)

    results = collection.query(
        query_texts=[text],
        n_results=10,
        where={"style": "style1"}
    )

    return results

def get_all_texts(username: str):
    collection_name = hashlib.sha256(username.encode()).hexdigest()
    collection = client.get_collection(name=collection_name)

    results = collection.query()

    return results
