from flask import Flask, send_from_directory
from flask_cors import CORS
import os

from config import Config
from database import db
from models.user import User
from models.apartment import Apartment

from routes.auth import auth
from routes.apartment import apartment_bp
from routes.notification import notification_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)

    app.register_blueprint(auth, url_prefix="/api/auth")
    app.register_blueprint(apartment_bp, url_prefix="/api/apartments")
    app.register_blueprint(notification_bp, url_prefix="/api/notifications")

    @app.route("/")
    def home():
        return {
            "message": "Apartment Vacancy Notifier API",
            "status": "Running"
        }

    with app.app_context():
        db.create_all()

    return app


app = create_app()

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)