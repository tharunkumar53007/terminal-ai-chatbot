from config import header, url
import requests
import json
from tokens import manage_conversation


messages = [
  {
    "role": "system",
    "content": "You are a friendly technical interviewer. ask user programming theory questions, ask only one question at a time. evaluate the answer. provide feedback and suggestions"
  }
]

def generate_response(messages):
  data = {
      "model" : "openai/gpt-oss-20b",
      "messages" : messages,
      "stream": True
    }
  try:
      response = requests.post(url=url,headers=header,json=data,timeout=30, stream=True)
      response.raise_for_status()

      ans = ""
      for line in response.iter_lines():
        if line:
          decoded_line = line.decode("utf-8")
          
          if decoded_line.startswith("data: "):
            chunk_data = decoded_line[6:]
            
            if chunk_data == "[DONE]":
              break
            
            chunk = json.loads(chunk_data)
            content = chunk["choices"][0]["delta"].get("content","")
            
            if content:
              ans+=content
      return ans
      
  except requests.exceptions.Timeout:
    raise
    
  except requests.exceptions.ConnectionError:
    raise
      
  except requests.exceptions.HTTPError as error:
    raise
      
  except requests.exceptions.RequestException as error:
    raise
      

if __name__ == "__main__":
  print("------welcome to the ChatBot-------")
  print("use q/quit to exit from ChatBot")
  while True:
    user = input("you: ")
    
    if(user == "q" or user == "quit"):
      break
    messages.append({
      "role" : "user",
      "content" : user
    })
    messages = manage_conversation(messages=messages,limit=50)
    data = {
      "model" : "openai/gpt-oss-20b",
      "messages" : messages,
      "stream": True
    }
    try:
      response = requests.post(url=url,headers=header,json=data,timeout=30, stream=True)
      response.raise_for_status()

      ans = ""
      print("AI : ",end="")
      for line in response.iter_lines():
        if line:
          decoded_line = line.decode("utf-8")
          
          if decoded_line.startswith("data: "):
            chunk_data = decoded_line[6:]
            
            if chunk_data == "[DONE]":
              break
            
            chunk = json.loads(chunk_data)
            content = chunk["choices"][0]["delta"].get("content","")
            
            if content:
              print(content, end="", flush=True)
              ans+=content
      
      print()
      messages.append({
        "role" : "assistant",
        "content" : ans
      })
    except requests.exceptions.Timeout:
      print("AI is taking too long, Try Again.")
      messages.pop()
      continue
    
    except requests.exceptions.ConnectionError:
      print("Connection failed. check your internet.")
      messages.pop()
      continue
      
    except requests.exceptions.HTTPError as error:
      print("API Error : ",error)
      messages.pop()
      continue
      
    except requests.exceptions.RequestException as error:
      print("Request failed : ",error)
      messages.pop()
      continue
  