from flask import Flask

class API:
    app = Flask(__name__)
    def __init__(self):
        self.app.run(port = 1337, debug=True)

    @app.route("/")
    def index():
        return "Hello World"
    
    