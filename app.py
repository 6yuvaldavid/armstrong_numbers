from flask import Flask, request, jsonify
from findarmstrong import find_armstrong

app = Flask(__name__)


@app.route("/ping")
def health_check():
    return "pong"


@app.route("/find", methods=["POST"])
def find_request():
    content = request.get_json()
    return jsonify(find_armstrong(content))


if __name__ == '__main__':
    app.run(debug=True)