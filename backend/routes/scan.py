from flask import Blueprint, request, jsonify
from services.url_scanner import scan_url

scan_blueprint = Blueprint('scan', __name__)

@scan_blueprint.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    result = scan_url(url)
    return jsonify(result)