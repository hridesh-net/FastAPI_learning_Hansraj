import os
import requests # module to make HTTP requests/calls

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

app = FastAPI(title="Grok Chat", version="0.1.0", description="API for Grok platform communication and LLM responses")

GROQ_BASE_URL = "https://api.groq.com/openai/v1"

class ChatRequestSchema(BaseModel):
    user_input: str
    model: str = "llama-3.3-70b-versatile" # models which needs to be used for LLM response
    max_tokens: int = 1000 # defines the length of response from the LLM model


@app.get("/")
def read_root():
    return {"message": "Welcome to Grok Chat API"}



@app.post("/chat")
def chat_with_grok_api(req: ChatRequestSchema):
    # Placeholder for Grok API interaction logic
    
    TOP_K = 10  # Number of top relevant documents to retrieve
    TEMPERATURE = 0.7  # Controls the randomness of the LLM's output
    
    api_key = os.getenv("GROK_API_KEY") # Retrieve Grok API key from environment variables
    
    if not api_key:
        print("Grok API key not found. Please set the GROK_API_KEY environment variable.")
        return {"error": "Internal server error"}
    
    print("Received request:")
    print(req)
    print("------------------")
    
    chat_completion_endpoint = f"{GROQ_BASE_URL}/chat/completions"
    
    auth_headers = f"Bearer {api_key}"  # Authorization header value / auth bearer token
    
    data = {
        "model": req.model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Expertise in tech domain like Python programming, software development, and AI/ML concepts"},  # System message
            {"role": "user", "content": req.user_input}
        ],
        "max_tokens": req.max_tokens,
    }
    
    """in request function we pass params as:
    - endpoint URL: where you have to send/hit the request
    - headers: authorization headers like API key or bearer token to verify Identity of the user
    - json: data/payload in JSON(in python its in dictionary format) format to be sent in the request body
    """
    
    resp = requests.post(
        chat_completion_endpoint,
        headers={"Authorization": auth_headers},
        json=data
    )
    
    response = {"response": resp.json()}
    return response
