from security.analysis_service import analyze_url
from flask import Blueprint, request, jsonify

scan_blueprint = Blueprint('scan', __name__)

@scan_blueprint.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    result = analyze_url(url)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)