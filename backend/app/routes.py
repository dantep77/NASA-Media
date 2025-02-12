from flask import Blueprint, request, jsonify
from app.nasa_api import search_nasa

api_blueprint = Blueprint("api", __name__)

@api_blueprint.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400

    data = search_nasa(query)
    count = data.length

    return jsonify({
        "count": count,
        "results": data
    })
