import pytest
from app.services.openai import query_openai


@pytest.fixture
def sample_messages():
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]


def test_query_openai(sample_messages):
    response = query_openai(sample_messages)
    assert isinstance(response, str)
    assert len(response) > 0

