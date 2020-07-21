import sys
import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from paths import ROOT_DIR
import wave

app = Flask(__name__)
socketio = SocketIO(app)

print(ROOT_DIR)

@app.route('/', methods=['POST', 'GET'])
def index():
    path = os.path.join('index.html')
    return render_template(path)


@socketio.on('catch-frame')
def catch_frame(data):
    print('receive: ' + data)

    ## getting the data frames

    ## do some processing

    ## send it back to client
    emit('response_back', 'receive')


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5000)
