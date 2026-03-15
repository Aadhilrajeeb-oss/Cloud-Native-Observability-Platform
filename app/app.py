from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import logging

app = FastAPI()

REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")

logging.basicConfig(level=logging.INFO)

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    logging.info("Home endpoint accessed")
    return {"message": "Cloud Observability Demo App"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")