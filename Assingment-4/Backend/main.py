from flask import Flask  # flask is what i'm using to make the backend
from config import Config
from routes import main_bp

def create_app():
    app = Flask(__name__)  # create flask app
    app.config.from_object(Config)  # load config
    app.register_blueprint(main_bp)  # set up routes
    return app

if __name__ == "__main__":
    app = create_app()  # make the app
    app.run(debug=True)  # run it