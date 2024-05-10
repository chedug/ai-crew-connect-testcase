from flask import Blueprint, request, jsonify
from app.services.training import train_agent

bp = Blueprint('training', __name__)


@bp.route('/train', methods=['POST'])
def train():
    """Train the AI agent based on provided sample data."""
    try:
        data = request.get_json()
        return train_agent(data)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

