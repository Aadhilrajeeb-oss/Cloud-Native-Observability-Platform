from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import logging
from fastapi import Request
from jose import jwt

SECRET="devopssecret"

def verify_token(request:Request):

 token=request.headers.get("Authorization")

 if not token:
  return None

 try:
  token=token.replace("Bearer ","")
  payload=jwt.decode(token,SECRET,algorithms=["HS256"])
  return payload
 except:
  return None
 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REQUESTS = Counter("task_requests_total", "Total task API requests")

logging.basicConfig(level=logging.INFO)

tasks = []

@app.get("/")
def home():
    REQUESTS.inc()
    return {"message": "Task Service Running"}

@app.post("/tasks")
def create_task(task:dict, request:Request):

    user=verify_token(request)

    if not user or user["role"]!="admin":
        logging.warning(f"Unauthorized task creation attempt by {user}")
        return {"error":"admin privileges required"}

    logging.info(f"Task created by {user['user']}")

    tasks.append(task)

    return {"status":"task added"}


@app.get("/tasks")
def get_tasks(request: Request):

    user = verify_token(request)

    if not user:
        return {"error": "Invalid token"}

    REQUESTS.inc()
    return tasks

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")