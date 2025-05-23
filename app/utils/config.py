import os
from app.utils.redis_client import redis_client


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    #
    CACHE_DEFAULT_TIMEOUT = 1800  # Default timeout of 30 minutes
    CACHE_TYPE = os.getenv("CACHE_TYPE", "SimpleCache")  # 'redis or 'SimpleCache'
    if CACHE_TYPE == "redis":
        SESSION_REDIS = redis_client
        SESSION_TYPE = "redis"
    # PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
