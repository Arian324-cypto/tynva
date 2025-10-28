from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Tynva Backend API 🚀"})

@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()
    return jsonify({"received": data, "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
