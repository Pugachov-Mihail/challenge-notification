from envparse import Env

env = Env()

MONGO_DB_URL = env.str(
    "MONGO_DB_URL",
    default="mongodb://root:1234@localhost:27017/"
)

REDIS_DB_URL = env.str(
    "REDIS_DB_URL",
    default = "redis://localhost:6379"
)