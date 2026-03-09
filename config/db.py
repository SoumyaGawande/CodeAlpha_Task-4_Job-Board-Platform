from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["job_board"]

employers_collection = db["employers"]
jobs_collection = db["jobs"]
candidates_collection = db["candidates"]
applications_collection = db["applications"]