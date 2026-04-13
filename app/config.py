import os
from ssm import get_parameter

ENV = os.getenv("APP_ENV", "local")


def _get(name: str, fallback_env: str):
    # local에서는 env 사용
    if ENV == "local":
        value = os.getenv(fallback_env)
        if not value:
            raise ValueError(f"{fallback_env} not set")
        return value

    # prod에서는 SSM
    return get_parameter(name)


DB_WRITER_HOST = _get(
    "/prod/ticketing/db/writer-endpoint",
    "DB_WRITER_HOST"
)

DB_READER_HOST = _get(
    "/prod/ticketing/db/reader-endpoint",
    "DB_READER_HOST"
)

DB_PASSWORD = _get(
    "/prod/ticketing/db/password",
    "DB_PASSWORD"
)

REDIS_HOST = _get(
    "/prod/ticketing/redis/endpoint",
    "REDIS_HOST"
)

SQS_URL = _get(
    "/prod/ticketing/sqs/url",
    "SQS_URL"
)