from app.extensions import db
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime


class WeatherCache(db.Model):
    __tablename__ = "weather_cache"

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100), nullable=False, index=True)
    result = db.Column(JSONB, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    __table_args__ = (
        db.Index("ix_weather_cache_location_updated_at", "location", "updated_at"),
    )
