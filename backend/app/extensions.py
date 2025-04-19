from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from app.configs import configs


db = SQLAlchemy()
redis_client = Redis.from_url(configs.redis_url)