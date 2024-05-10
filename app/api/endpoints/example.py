from flask import jsonify, request, Blueprint
from app.db.client import db

bp = Blueprint('example', __name__)


@bp.route('/get_items', methods=['GET'])
def get_items():
    items_ref = db.collection('test')
    docs = items_ref.stream()
    items = [{doc.id: doc.to_dict()} for doc in docs]
    return jsonify(items), 200


@bp.route('/add_item', methods=['POST'])
def add_item():
    try:
        data = request.json
        doc_ref = db.collection('test').document()
        doc_ref.set(data)
        return jsonify({"success": True, "id": doc_ref.id}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

