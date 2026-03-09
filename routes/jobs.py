from flask import Blueprint, request, jsonify
from config.db import jobs_collection
from utils.serializer import serialize_doc

jobs = Blueprint("jobs", __name__)

@jobs.route("/jobs", methods=["POST"])
def create_job():

    data = request.get_json()

    job = {
        "title": data.get("title"),
        "description": data.get("description"),
        "salary": data.get("salary"),
        "employer_id": data.get("employer_id")
    }

    result = jobs_collection.insert_one(job)

    job["_id"] = str(result.inserted_id)

    return jsonify({
        "message": "Job posted",
        "job": job
    }), 201


@jobs.route("/jobs", methods=["GET"])
def get_jobs():

    keyword = request.args.get("title")

    if keyword:
        jobs = jobs_collection.find(
            {"title": {"$regex": keyword, "$options": "i"}}
        )
    else:
        jobs = jobs_collection.find()

    result = [serialize_doc(job) for job in jobs]

    return jsonify(result), 200