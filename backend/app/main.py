from flask.cli import FlaskGroup
from app.app import create_app
from app.extensions import db
from app.api.weather.models import WeatherCache  # import your models here

app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
