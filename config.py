import os

from starlette.config import Config

config = Config(".env")

RAW_DB_URL = os.environ.get('DB_URL')

if RAW_DB_URL is None:
    RAW_DB_URL = 'postgresql://postgres_user:geodata1234@127.0.0.1:5444/postgres' # noqa

DB_URL = config(
    "DB_URL",
    cast=str,
    default=RAW_DB_URL
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
