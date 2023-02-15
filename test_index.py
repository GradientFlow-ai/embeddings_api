from fastapi.testclient import TestClient
import json

from index import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

    reply = {'message': 'Hello from the embeddings service, we are cooking now!'}
    assert response.json() == reply


def test_post_json():

    response = client.put(
        "/embed_text",
        headers={"X-Token": "coneofsilence"},
        json={"document": "This is a test document to be embedded."},
    )
    assert response.status_code == 200

    decoded_response = response.json()
    assumed_response = {'message': 'we got your document', 'data': {'document': 'This is a test document to be embedded.'}}

    assert decoded_response == assumed_response
