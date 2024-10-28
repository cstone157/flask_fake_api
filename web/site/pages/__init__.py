from flask import Blueprint, jsonify

def create_blueprint():
    bp = Blueprint("pages", __name__)

    @bp.route("/")
    def home():
        return "Hello, World!"

    @bp.route('/greet/<string:name>', methods=['GET'])
    def greet(name):
        return jsonify(message=f"Hello, {name}!")

    return bp