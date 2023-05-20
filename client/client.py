import socketio

sio = socketio.Client(logger=True)

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('chat message')
def handle_message(msg):
    print('Received message:', msg)

sio.connect('http://localhost:8080')

while True:
    message = input('Enter a message: ')
    sio.emit('chat message', message)