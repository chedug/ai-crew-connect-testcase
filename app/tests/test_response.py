import pytest
from app.main import app
from app.db.client import db


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def sample_training_data():
    return {
        "role": "Sales Manager",
        "sample_data": [
            {
                "input": "Can you provide a new pricing strategy?",
                "output": "Certainly! Here are some ideas for the new strategy..."
            },
            {
                "input": "What should be our approach for the upcoming marketing campaign?",
                "output": "We should target potential clients in the tech sector."
            }
        ]
    }


@pytest.fixture
def sample_conversation():
    return {
        "role": "Sales Manager",
        "conversation": [
            {
                "input": "Can you provide a new pricing strategy?",
                "output": "Certainly! Here are some ideas for the new strategy..."
            },
            {
                "input": "What should be our approach for the upcoming marketing campaign?"
            }
        ]
    }


def test_respond_endpoint(client, sample_training_data, sample_conversation):
    # First, store the training data
    client.post('/train', json=sample_training_data)

    # Test the response generation
    response = client.post('/respond', json=sample_conversation)
    assert response.status_code == 200
    assert response.json["success"] is True
    assert len(response.json["response"]) > 0

    # Check if the response was stored in Firestore
    responses_ref = db.collection('responses')
    docs = responses_ref.stream()
    assert len([doc for doc in docs]) > 0
