import os, json
from flask import Flask, render_template, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():
    with open(os.path.join(BASE_DIR, "data.json"), encoding="utf-8") as f:
        return json.load(f)
    
app = Flask(__name__)

@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", data=data["index"])

@app.route("/subject")
def subject_page():
    data = load_data()
    return render_template("subject.html", data=data["subject"])

@app.route("/rationale")
def rationale_page():
    data = load_data()
    return render_template("rationale.html", data=data["rationale"])

@app.route("/features")
def features_page():
    data = load_data()
    return render_template("features.html", data=data["features"])

@app.route("/environment")
def environment_page():
    data = load_data()
    return render_template("environment.html", data=data["environment"])

@app.route("/team")
def team_page():
    data = load_data()
    return render_template("team.html", data=data["team"])

# API 라우트
@app.route("/api/<section>")
def api(section):
    data = load_data()
    if section in data:
        return jsonify(data[section])
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)