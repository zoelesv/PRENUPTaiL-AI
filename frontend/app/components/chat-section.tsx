"use client";

import React, { useRef, useState, useEffect } from 'react';

const mockMessages = [
  {
    text: "Hi there, I've been pondering the concept of knowledge graphs lately.",
    left: true,
  },
  {
    text: "Ah, knowledge graphs! They're quite fascinating. They enable machines to understand and interpret complex data in a more human-like manner.",
    left: false,
  },
  {
    text: "Exactly! By structuring data as graphs, they can represent semantic relationships between various entities.",
    left: true,
  },
  {
    text: "Indeed, and this structure allows for more nuanced querying and data retrieval. It's a key technology behind many AI applications.",
    left: false,
  },
  {
    text: "I'm particularly interested in how knowledge graphs can evolve. They're not static, after all. They grow as new information is discovered and added.",
    left: true,
  },
  {
    text: "That's a good point. The dynamic nature of knowledge graphs means they can adapt to new contexts and understandings, making them incredibly powerful for AI.",
    left: false,
  },
  {
    text: "And let's not forget the challenges in creating and maintaining them. Ensuring data accuracy and dealing with ambiguity is no small feat.",
    left: true,
  },
  {
    text: "Certainly, there's a lot of ongoing research in that area. Techniques like machine learning can help automate the process, but human oversight is still crucial.",
    left: false,
  },
  {
    text: "It's an exciting field, and I'm eager to see how knowledge graphs will shape the future of AI and data analysis.",
    left: true,
  },
  {
    text: "As am I. Their potential is vast, and we're just beginning to scratch the surface of what's possible.",
    left: false,
  },
];
type Message = {
  text: string;
  left: boolean;
};

export default function ChatSection() {
  const msgEndRef = useRef<HTMLDivElement>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentMessageIndex, setCurrentMessageIndex] = useState(0);

  useEffect(() => {
    if (currentMessageIndex < mockMessages.length) {
      //console.log(mockMessages[currentMessageIndex].text.length*100);
      let delay = mockMessages[currentMessageIndex].text.length*20;
      const timer = setTimeout(() => {
        setMessages(prevMessages => [...prevMessages, mockMessages[currentMessageIndex]]);
        setCurrentMessageIndex(prevIndex => prevIndex + 1);
      }, delay);

      return () => clearTimeout(timer);
    }
  }, [currentMessageIndex, mockMessages.length]);


  // Scroll to the bottom of the chat when new messages are added
  useEffect(() => {
    if (msgEndRef.current) {
      msgEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <div className="chatbox rounded-xl shadow-xl">
      <div className="chat-container">
        {messages.map ((message, i) =>
            <div key={i} className={message.left?"chat left  shadow-xl": "chat right  shadow-xl"}>
                <img className= 'chatImg' src={message.left?"/gptlogo.png":"/llama.png"}/>
                <p className='text'>{message.text}</p>
            </div>
            )}
        <div ref={msgEndRef}/>
      </div>
    </div>
  );
}
