from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import generate_response

class ChatRequest(BaseModel):
  conversation_id : str
  message : str

app = FastAPI()

conversations = {}

@app.get("/")
def greeting():
  return {
    "message" : "Ai chatbot API is Running.."
  }
  
@app.post("/chat")
def chat(request : ChatRequest):
  
  if request.conversation_id not in conversations:
    conversations[request.conversation_id] = []
  
  messages = conversations[request.conversation_id]
  
  messages.append({
    "role": "user",
    "content": request.message
  })
  
  answer = generate_response(messages=messages)
  
  messages.append({
    "role": "assistant",
    "content":answer
  })
  
  return {
    "response" : answer
  }