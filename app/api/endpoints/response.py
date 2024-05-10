from flask import Blueprint, request, jsonify
from app.services.response import generate_response, get_responses

bp = Blueprint('responses', __name__)


@bp.route('/respond', methods=['POST'])
def respond():
    """Generate a response from the AI agent."""
    try:
        data = request.json
        return generate_response(data)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@bp.route('/responses', methods=['GET'])
def responses():
    """Retrieve all generated responses."""
    try:
        return get_responses()
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
