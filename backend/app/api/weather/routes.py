from flask import Blueprint, request, jsonify
import requests
from app.extensions import db, redis_client
from .models import WeatherCache
from .services import fetch_weather_from_api
from datetime import datetime, timedelta, timezone
import json

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/")
def get_weather():
    location = request.args.get("location")
    if not location:
        return jsonify({"error": "Missing 'location' parameter"}), 400
    cache_key = f"weatherapi:{location.lower()}"
    if redis_data := redis_client.get(cache_key):
        return jsonify(json.loads(redis_data))
    one_hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)
    db_cache = (
        WeatherCache.query.filter(WeatherCache.location == location)
        .filter(WeatherCache.updated_at >= one_hour_ago)
        .order_by(WeatherCache.updated_at.desc())
        .first()
    )
    if db_cache:
        redis_client.setex(cache_key, 60, json.dumps(db_cache.result))
        return jsonify(db_cache.result)
    data = fetch_weather_from_api(location)
    db.session.add(WeatherCache(location=location, result=data))
    db.session.commit()
    redis_client.setex(cache_key, 60, json.dumps(data))
    return jsonify(data)
