import threading
from flask import Flask, jsonify

class ServerSpawn(threading.Thread):
    def __init__(self, port):
        self.port = port
        self.app = Flask(__name__)
        self.app.add_url_rule('/', 'index', self.index)
        threading.Thread.__init__(self)

    def index(self):                
        return jsonify(port=self.port)        

    def run(self):
        self.runFlask()

    def runFlask(self):
        self.app.run('127.0.0.1', self.port, False)
        