from flask import Blueprint, request, jsonify
from config.db import applications_collection
from utils.serializer import serialize_doc

applications = Blueprint("applications", __name__)

@applications.route("/apply", methods=["POST"])
def apply_job():

    data = request.get_json()

    application = {
        "job_id": data.get("job_id"),
        "candidate_id": data.get("candidate_id"),
        "status": "applied"
    }

    result = applications_collection.insert_one(application)

    application["_id"] = str(result.inserted_id)

    return jsonify({
        "message": "Application submitted",
        "application": application
    }), 201


@applications.route("/applications/<candidate_id>", methods=["GET"])
def get_applications(candidate_id):

    apps = applications_collection.find({
        "candidate_id": candidate_id
    })

    result = [serialize_doc(app) for app in apps]

    return jsonify(result), 200