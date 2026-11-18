import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
  raise ValueError("API key not found!")

url = "https://api.groq.com/openai/v1/chat/completions"

header = {
  "Authorization":f"Bearer {api_key}",
  "Content-Type":"application/json"
}