from flask import Flask, jsonify, request
from database import get_database
from ai_voice import voice_to_text, translate_text

app = Flask(__name__)
db = get_database()

@app.route('/')
def home():
    return jsonify({"message": "🌐 Tynva Integration Server Running Successfully!"})

@app.route('/ai/voice', methods=['POST'])
def ai_voice():
    lang = request.json.get('lang', 'bn')
    target_lang = request.json.get('target', 'en')
    text = voice_to_text(lang)
    if text:
        translated = translate_text(text, target_lang)
        return jsonify({"original": text, "translated": translated})
    return jsonify({"error": "Voice recognition failed"})

@app.route('/users', methods=['GET'])
def users():
    users = list(db["users"].find({}, {"_id": 0}))
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
