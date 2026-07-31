from flask import Flask
from flask_cors import CORS

from config import Config
from database import db

# Import Blueprints
from routes.auth import auth
from routes.apartment import apartment_bp
from routes.notification import notification_bp


def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Initialize database
    db.init_app(app)

    # Register routes
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

if __name__ == "__main__":
    app.run(debug=True)