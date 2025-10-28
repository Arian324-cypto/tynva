from flask import Blueprint, request, jsonify
from database import get_database
from datetime import datetime

chat_bp = Blueprint('chat', __name__)
db = get_database()
messages = db["messages"]

@chat_bp.route('/chat/send', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    receiver = data.get('receiver')
    message = data.get('message')
    timestamp = datetime.utcnow().isoformat()

    messages.insert_one({
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "timestamp": timestamp
    })
    return jsonify({"status": "sent", "timestamp": timestamp})

@chat_bp.route('/chat/get', methods=['POST'])
def get_messages():
    data = request.get_json()
    user1 = data.get('user1')
    user2 = data.get('user2')

    chat_data = list(messages.find({
        "$or": [
            {"sender": user1, "receiver": user2},
            {"sender": user2, "receiver": user1}
        ]
    }, {"_id": 0}).sort("timestamp", 1))

    return jsonify({"conversation": chat_data})
