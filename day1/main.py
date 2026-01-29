from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/")
def hello_folks():
    return {"message": "Hello, folks! from FastAPI"}

@app.post("/student")
def create_student(data: Student):
    return {
        "message": "Student created successfully",
        "student": data
    }

USERS = {
    "1a": {"name": "Alice", "age": 21},
    "2b": {"name": "Bob", "age": 22},
    "3a": {"name": "Charlie", "age": 23},
}    


@app.get("/user/{user_id}") # user_id is a path parameter
def get_user(user_id: str):
    user = USERS.get(user_id) # user_id is not there in USERS then this will return None
    """ USERS[user_id] -> KeyError if user_id not found"""
    if user:
        return {"user_id": user_id, "user": user}
    
    return {"message": "User not found"}

@app.get("/users") # for query params we don't have to mention anythng in endpoint declaration
def get_all_users(user_id: str = None): # for query params we have to provide default value and the keys
    if user_id:
        user = USERS.get(user_id)
        if user:
            return {"user_id": user_id, "user": user}
        return {"message": "User not found"}
    
    # if no query or user_id then return all users
    return {"users": USERS}