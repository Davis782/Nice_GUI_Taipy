# BackEnd.py
from taipy.gui import Gui
from flask import Flask, request, jsonify
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(flask_app)  # Enable CORS for all routes

@flask_app.route("/data1", methods=['GET'])
def data1():
    return jsonify({"message": "Data from backend - Route 1"})

@flask_app.route("/data2", methods=['POST'])
def data2():
    data = request.get_json()
    name = data.get("name", "No Name Provided")
    return jsonify({"message": f"Hello, {name}! - Route 2"})

@flask_app.route("/data3", methods=['GET'])
def data3():
    return jsonify({"message": "Data from backend - Route 3"})

@flask_app.route("/data4", methods=['POST'])
def data4():
    data = request.get_json()
    number = data.get("number", "No Number Provided")
    return jsonify({"message": f"Your Number is: {number}! - Route 4"})

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=8082, debug=True) # Expose to all interfaces for Docker