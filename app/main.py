from fastapi import FastAPI
from config import DB_WRITER_HOST, REDIS_HOST

app = FastAPI()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "db": DB_WRITER_HOST,
        "redis": REDIS_HOST
    }