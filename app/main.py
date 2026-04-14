from fastapi import FastAPI
from app.config import get_db_config

app = FastAPI()

@app.get("/ssm-test")
def ssm_test():
    return get_db_config()