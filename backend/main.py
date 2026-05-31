# backend/main.py
from fastapi import FastAPI

# start the application
app = FastAPI(title="NextRole.ai API")

@app.get("/")
def read_root():
    return {"message": "FastAPI server for NextRole.ai is online!"}