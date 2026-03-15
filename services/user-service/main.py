from fastapi import FastAPI
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("user_service_requests_total", "Total API Requests")

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    logging.info("Home endpoint accessed")
    return {"service": "User Service Running"}

@app.get("/users")
def get_users():
    REQUEST_COUNT.inc()
    logging.info("Fetching users")
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")