from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt
from datetime import datetime, timedelta

import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def audit(message):
    logging.info(message)

SECRET="devopssecret"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

users = {
 "admin":{"password":"admin123","role":"admin"},
 "dev":{"password":"dev123","role":"developer"},
 "viewer":{"password":"view123","role":"viewer"}
}

@app.get("/users")
def list_users():
    return [{"username":u,"role":users[u]["role"]} for u in users]
@app.post("/users")
def create_user(data:dict):

    username=data["username"]
    password=data["password"]
    role=data["role"]

    if username in users:
        return {"error":"user exists"}

    users[username]={"password":password,"role":role}

    audit(f"User {username} created with role {role}")

    return {"status":"user created"}

@app.put("/users/{username}")
def update_role(username:str,data:dict):

    if username not in users:
        return {"error":"user not found"}

    role=data["role"]

    users[username]["role"]=role

    audit(f"Role of {username} updated to {role}")

    return {"status":"role updated"}

@app.post("/login")
def login(data:dict):

    username=data["username"]
    password=data["password"]

    user=users.get(username)

    if not user or user["password"]!=password:
        audit(f"FAILED login attempt for user {username}")
        return {"error":"invalid credentials"}

    audit(f"{username} logged in successfully")

    token=jwt.encode(
    {
        "user":username,
        "role":user["role"]
    },
    SECRET,
    algorithm="HS256"
    )

    return {"token":token,"role":user["role"]}