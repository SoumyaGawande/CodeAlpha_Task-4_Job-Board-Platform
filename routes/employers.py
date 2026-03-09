from flask import Blueprint, request, jsonify
from config.db import employers_collection
from utils.serializer import serialize_doc

employers = Blueprint("employers", __name__)

@employers.route("/employers", methods=["POST"])
def create_employer():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    employer = {
        "company_name": data.get("company_name"),
        "email": data.get("email")
    }

    result = employers_collection.insert_one(employer)

    employer["_id"] = str(result.inserted_id)

    return jsonify({
        "message": "Employer created",
        "employer": employer
    }), 201