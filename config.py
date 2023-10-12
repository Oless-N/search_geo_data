from starlette.config import Config

config = Config(".env")

DB_URL = config(
    "DB_URL",
    cast=str,
    default="postgresql://postgres_user:geodata1234@127.0.0.1:5444/postgres",
)

HOST = config(
    "DB_URL",
    cast=str,
    default="127.0.0.1",
)

PORT = config(
    "DB_URL",
    cast=int,
    default=8989,
)

prefix = '/api/v1'
