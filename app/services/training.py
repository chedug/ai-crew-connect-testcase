from flask import jsonify
from app.db.client import db
from app.models.training import TrainingData
from app.models.firestore_models import Training



def train_agent(data):
    """Train the AI agent based on provided sample data."""
    try:
        training_data = TrainingData(**data)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

    role = training_data.role
    sample_data = training_data.sample_data

    messages = [
        {"role": "system", "content": f"Training a {role} agent."}
    ]
    for example in sample_data:
        messages.append({"role": "user", "content": example.input})
        messages.append({"role": "assistant", "content": example.output})

    training = Training(role=role, messages=messages)
    training_ref = db.collection('training').document(role)
    training_ref.set(training.dict())

    return jsonify({"success": True, "message": f"{role} training data stored"}), 201
