from fastapi import FastAPI

app = FastAPI(title="AIOps Root Cause Platform")


@app.get("/health")
def health():
    return {"status": "ok"}