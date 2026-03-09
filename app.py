from flask import Flask
from flask_cors import CORS

from routes.employers import employers
from routes.jobs import jobs
from routes.candidates import candidates
from routes.applications import applications

app = Flask(__name__)

CORS(app)

app.register_blueprint(employers)
app.register_blueprint(jobs)
app.register_blueprint(candidates)
app.register_blueprint(applications)

@app.route("/")
def home():
    return {"message": "Job Board API running"}

if __name__ == "__main__":
    app.run(debug=True)