# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    """Adds two numbers and returns the sum."""
    return jsonify({'result': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True)
