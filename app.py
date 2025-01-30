from flask import Flask, Response, jsonify
from datetime import datetime
import pytz
import json
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def get_info():
    current_time = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ')

    info = OrderedDict([
        ("email", "rodiathammed48@gmail.com"),
        ("current_datetime", current_time),
        ("github_url", "https://github.com/codefromlani/Public-API")
    ])

    json_response = json.dumps(info)
    return Response(json_response, mimetype='application/json')

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found got to /api"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)