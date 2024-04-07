"use client";

import { useChat } from "ai/react";
import { ChatInput } from "./ui/chat";
import Header from "@/app/components/header";

export default function InputSection() {
  const {
    input,
    isLoading,
    handleSubmit,
    handleInputChange,
  } = useChat({
    api: process.env.NEXT_PUBLIC_CHAT_API,
    headers: {
      "Content-Type": "application/json", // using JSON because of vercel/ai 2.2.26
    },
  });

  return (
    <div className="space-y-4 max-w-5xl w-full">
        <aside className={`left-column 'visible' : 'show'} w-full`}>
          {/* Left column content goes here */
          <div>
            <Header />
            <ChatInput
            input={input}
            handleSubmit={handleSubmit}
            handleInputChange={handleInputChange}
            isLoading={isLoading}
            multiModal={process.env.NEXT_PUBLIC_MODEL === "gpt-4-vision-preview"}
          />
        </div>}
        </aside>
    </div>
  );
}
