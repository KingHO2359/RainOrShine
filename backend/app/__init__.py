from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.configs import configs
from app.extensions import db

migrate = Migrate()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = configs.database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.weather.routes import weather_bp
    app.register_blueprint(weather_bp, url_prefix="/api/weather")

    return app
