import os

from fastapi import FastAPI

app = FastAPI(title="tums")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}


@app.get("/hello")
def hello():
    return {"message": "world"}


@app.get("/env")
def get_env():
    return {
        "ENVIRONMENT": os.environ.get("ENVIRONMENT"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL"),
    }


@app.get("/secret")
def get_secret():
    return {"MY_SECRET": os.environ.get("MY_SECRET")}
