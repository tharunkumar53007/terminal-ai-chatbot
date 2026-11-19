import './App.css'
import { useState } from 'react'

function ChatHeader({title})
{
  return (
    <div>
      <h2>{title}</h2>
    </div>
  )
}

function App() {
  const [input, setInput] = useState("")
  return (
    <div className="app">

      <aside className="sidebar">
        <ChatHeader title="AI Chatbot"/>
        <button>+ New Chat</button>
      </aside>

      <main className="chat-area">
        <ChatHeader title="New Conversation"/>

        <section className="messages">
          <h3>Welcome to AI Chatbot</h3>
          <p>How can I help you today?</p>
        </section>

        <footer className="chat-input">
          <input
            type="text"
            placeholder="Ask Anything"
            value={input}
            onChange={(e) => setInput(e.target.value)} 
          />
          <button>Send</button>
        </footer>

      </main>

    </div>
  )
}

export default App