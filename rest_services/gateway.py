from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SERVERS = {
    "CtoF": "http://127.0.0.1:5001/",
    "FtoC": "http://127.0.0.1:5002/"
}

@app.route('/convert', methods=['GET'])
def route_request():
    value = request.args.get('value')
    conversion_type = request.args.get('type')

    api_url = SERVERS.get(conversion_type)

    response = requests.get(api_url, params={'value': value})
    data = response.json()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5003)

