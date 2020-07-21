from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from paths import ROOT_DIR
import os


app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    path = os.path.join(ROOT_DIR, 'FrontEnd/index.html')
    return render_template(path)


@socketio.on('catch-frame')
def catch_frame(data):

    ## getting the data frames

    ## do some processing

    ## send it back to client
    emit('response_back', data)  ## ??


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1')
