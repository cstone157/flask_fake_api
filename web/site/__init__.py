from flask import Flask

#from server 
from .pages import create_blueprint

def create_app():
    app = Flask(__name__)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)

    bp = create_blueprint()
    app.register_blueprint(bp)
    return app