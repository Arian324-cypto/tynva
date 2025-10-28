from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return "📞 Tynva Call Server is Live!"

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': f"{data['user']} joined room {room}"}, room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    emit('status', {'msg': f"{data['user']} left room {room}"}, room=room)

@socketio.on('signal')
def handle_signal(data):
    emit('signal', data, room=data['room'], include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
