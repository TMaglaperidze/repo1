from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/get-name', methods=['GET'])
def get_name():
    name = os.getenv('NAME', '')
    if name:
        return jsonify({"name": name})
    else:
        return jsonify({"error": "Name is empty"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
