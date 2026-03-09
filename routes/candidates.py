from flask import Blueprint, request, jsonify
from config.db import candidates_collection

candidates = Blueprint("candidates", __name__)

@candidates.route("/candidates", methods=["POST"])
def create_candidate():

    data = request.get_json()

    candidate = {
        "name": data.get("name"),
        "email": data.get("email"),
        "resume": data.get("resume")
    }

    result = candidates_collection.insert_one(candidate)

    candidate["_id"] = str(result.inserted_id)

    return jsonify({
        "message": "Candidate created",
        "candidate": candidate
    }), 201