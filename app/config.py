from app.ssm import get_ssm_parameter

ENV = "prod"

def get_db_config():
    return {
        "host": get_ssm_parameter(f"/{ENV}/ticketing/db/writer-endpoint"),
        "password": get_ssm_parameter(f"/{ENV}/ticketing/db/password", True),
    }