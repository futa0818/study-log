from flask import Flask

def create_app():
    app = Flask(__name__)

    from application.routes.main import main_bp
    app.register_blueprint(main_bp)

    from application.routes.logs import logs_bp
    app.register_blueprint(logs_bp)

    return app