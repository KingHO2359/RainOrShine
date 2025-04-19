import requests
from loguru import logger
from app.configs import configs

CURRENT_WEATHER_BASE_URL = "https://api.weatherapi.com/v1"

# Set up a shared session with default params
session = requests.Session()
session.params = {"key": configs.weatherapi_key}  # add default API key

def fetch_weather_from_api(location: str) -> dict:
    logger.info(f"Fetching weather data for {location} from WEATHER API")

    response = session.get(
        f"{CURRENT_WEATHER_BASE_URL}/current.json",
        params={"q": location}  # only need to pass the location
    )

    response.raise_for_status()
    return response.json()
