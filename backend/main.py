from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from motor.motor_asyncio import AsyncIOMotorClient

from model import Todo

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

MONGODB_USERNAME = os.getenv("MONGODB_USERNAME")
MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
MONGODB_HOSTNAME = os.getenv("MONGODB_HOSTNAME")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")

MONGODB_USERNAME = "myMongoUser"
MONGODB_PASSWORD = "myMongoPassword"
MONGODB_HOSTNAME = "mongodb-service"
MONGODB_DATABASE = "opsprod-database"

mongo_details = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOSTNAME}:27017/{MONGODB_DATABASE}"
mongo_details = "mongodb://localhost:27017"
client = AsyncIOMotorClient(mongo_details)
db = client[MONGODB_DATABASE]

app = FastAPI()

# Set up CORS to allow any origin - adjust this for production!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Warning: It's insecure to allow all origins in production.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")

