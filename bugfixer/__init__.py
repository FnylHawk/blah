from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register the routes from routes.py
    from bugfixer.routes import bugfixer_bp
    app.register_blueprint(bugfixer_bp)

    return app