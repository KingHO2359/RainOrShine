import requests
from loguru import logger
from app.configs import configs
from urllib.parse import urlencode

CURRENT_WEATHER_BASE_URL = "https://api.weatherapi.com/v1"


def fetch_weather_from_api(location: str) -> dict:
    logger.info(f"Fetching weather data for {location} from WEATHER API")

    encoded_params = urlencode({"key": configs.weatherapi_key, "q": location})
    url = f"{CURRENT_WEATHER_BASE_URL}/current.json?{encoded_params}"
    response = requests.get(url)

    response.raise_for_status()
    return response.json()
