from flask import jsonify
from firebase_admin import firestore
from app.models.conversation import ConversationData
from app.models.firestore_models import Response
import openai
import os
from app.services.openai import query_openai


openai.api_key = os.getenv('OPENAI_API_KEY')
db = firestore.client()


def generate_response(data):
    """Simulate agent response based on conversation dataset."""
    try:
        conversation_data = ConversationData(**data)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

    role = conversation_data.role
    conversation = conversation_data.conversation

    training_ref = db.collection('training').document(role)
    training_doc = training_ref.get()
    if not training_doc.exists:
        return jsonify({"success": False, "message": f"No training data for role {role}"}), 404

    training_messages = training_doc.to_dict()["messages"]

    for message in conversation:
        training_messages.append({"role": "user", "content": message.input})
        training_messages.append({"role": "assistant", "content": message.output if message.output else ""})

    generated_response = query_openai(training_messages)

    response = Response(role=role, conversation=[msg.dict() for msg in conversation], generated_response=generated_response)
    response_ref = db.collection('responses').document()
    response_ref.set(response.dict())

    return jsonify({"success": True, "response": generated_response}), 200


def get_responses():
    """Retrieve all generated responses from Firestore."""
    responses_ref = db.collection('responses')
    docs = responses_ref.stream()
    responses = [{doc.id: doc.to_dict()} for doc in docs]
    return jsonify(responses), 200
