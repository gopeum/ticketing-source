from app.config.ssm import get_parameter

ENV = "prod"

def get_db_config():
    return {
        "writer": get_parameter(f"/{ENV}/ticketing/db/writer-endpoint"),
        "reader": get_parameter(f"/{ENV}/ticketing/db/reader-endpoint"),
        "password": get_parameter(f"/{ENV}/ticketing/db/password"),
    }