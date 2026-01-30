from fastapi import FastAPI
from pydantic import BaseModel

# step 1: create FastAPI app instance
app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str


# Step 2: define endpoints
@app.get("/") # Decorator to define a GET endpoint (works on the concept of Abstraction in OOPs paradigm)
def hello_folks():
    """takes noting but returns a message "Hello, Folks! from FastAPI
    """
    
    return {"message": "Hello, folks! from FastAPI"}

@app.post("/student") # Decorator to define a POST endpoint
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
def get_user(user_id: str): # use the same name as in the path parameter
    
    user = USERS.get(user_id) # user_id is not there in USERS then this will return None
    """ USERS[user_id] -> KeyError if user_id not found"""
    if user:
        return {"user_id": user_id, "user": user}
    
    return {"message": "User not found"}

@app.get("/users") # for query params we don't have to mention anythng in endpoint declaration
def get_all_users(user_id: str = None, is_all: bool = False): # for query params we have to provide default value and the keys
    if user_id:
        user = USERS.get(user_id)
        if user:
            return {"user_id": user_id, "user": user}
        return {"message": "User not found"}
    
    # if no query or user_id then return all users
    if is_all:
        return {"users": USERS}
    
    return {"message": "No valid query parameters provided"}