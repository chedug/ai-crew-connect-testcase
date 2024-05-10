from flask import jsonify, request, Blueprint
from app.db.client import db

example_blueprint = Blueprint('example', __name__)


@example_blueprint.route('/')
def home():
    return "Welcome to the Flask Firebase microservice!"


@example_blueprint.route('/get_items', methods=['GET'])
def get_items():
    items_ref = db.collection('test')
    docs = items_ref.stream()
    items = [{doc.id: doc.to_dict()} for doc in docs]
    return jsonify(items), 200


@example_blueprint.route('/add_item', methods=['POST'])
def add_item():
    try:
        data = request.json
        doc_ref = db.collection('test').document()
        doc_ref.set(data)
        return jsonify({"success": True, "id": doc_ref.id}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

