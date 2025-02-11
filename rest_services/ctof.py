from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

@app.route('/', methods=['GET'])
def convert_temperature():
    value = float(request.args.get('value'))
    result = celsius_to_fahrenheit(value)
    return jsonify({'input': f"{value} Celsius", 'result': f"{round(result, 2)} Fahrenheit"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
