from pydantic_settings import BaseSettings

class AppConfigs(BaseSettings):
    database_url: str
    weatherapi_key: str
    redis_url: str

    class Config:
        env_file = ".env"

configs = AppConfigs()
