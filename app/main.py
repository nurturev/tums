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
