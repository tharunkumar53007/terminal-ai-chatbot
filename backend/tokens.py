import tiktoken
from summary import summarize_conversation


def count_tokens(text): 
  encoding = tiktoken.get_encoding("cl100k_base")
  tokens = encoding.encode(text=text)
  
  return len(tokens)

def count_conversation_tokens(messages):
  total = 0
  for message in messages:
    text = message["content"]
    total+=count_tokens(text=text)
  
  return total

def should_summarize(messages,limit):
  if count_conversation_tokens(messages=messages) > limit:
    return True
  
  return False

def manage_conversation(messages, limit):
  if should_summarize(messages=messages, limit=limit):
    if len(messages) <= 6:
      print("Not enough messages to summarize.")
      return messages
    print("Summarization Required!")
    system_message = messages[0]
    old_messages = messages[1:-4]
    recent_messages = messages[-4:]
    
    summary = summarize_conversation(old_messages=old_messages)
    summary_message = {
      "role" : "system",
      "content" : f"Previous conversation summary: {summary}"
    }
    
    messages = [system_message,summary_message] + recent_messages
    
    print("OLD MESSAGES:", old_messages)
    print("RECENT MESSAGES:", recent_messages)
    print("GENERATED SUMMARY:", summary)
        
  else:
    print("Conversation is within the token limit.")
    
  return messages
    