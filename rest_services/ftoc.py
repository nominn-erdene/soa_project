from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/', methods=['GET'])
def convert_temperature():
    value = float(request.args.get('value'))
    result = fahrenheit_to_celsius(value)
    return jsonify({'input': f"{value} Fahrenheit", 'result': f"{round(result, 2)} Celsius"})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
