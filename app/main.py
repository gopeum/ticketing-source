from fastapi import FastAPI
from app.config.settings import get_db_config

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ssm-test")
def ssm_test():
    return get_db_config()