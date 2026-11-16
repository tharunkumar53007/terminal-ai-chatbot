from config import header, url
import requests
import json


def summarize_conversation(old_messages):
  
  conversation_text = json.dumps(old_messages,indent=2)
  data = {
    "model" : "openai/gpt-oss-20b",
    "messages" : [
      {
        "role" : "system",
        "content": """
          Summarize the conversation into five sections:

          1. User Profile
          2. Skills
          3. Projects
          4. Preferences
          5. Conversation Context

          Instructions:
          - Preserve important facts from previous conversations.- Preserve only facts explicitly stated by the user.
          - Do not infer expertise, proficiency, experience, or achievements.
            from a user's education or list of skills.
          - Never add programming languages, frameworks, tools, or technologies
            that the user did not mention.
          - Distinguish confirmed facts from uncertain information.
          - Preserve updated information when the user corrects an earlier statement.
          """
      },
      {
        "role" : "user",
        "content" : conversation_text
      }
    ]
  }

  response = requests.post(url=url,headers=header, json=data, timeout=30)

  response.raise_for_status()

  result = response.json()

  summary = result["choices"][0]["message"]["content"]
  
  return summary