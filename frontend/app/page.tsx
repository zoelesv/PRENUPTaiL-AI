import ChatSection from "./components/chat-section";
import InputSection from "./components/input-section";
import PlayBar from "./components/playbar";

export default function Home() {

  return (
    <main className="flex min-h-screen flex-col items-center gap-10 px-2 md:px-6 py-2 md:py-6 background-gradient">
      <div className="flex w-full flex-col md:flex-row">
        <section className="md:w-2/5 w-screen overflow-auto">
          <InputSection />
        </section>
        <section className="md:w-3/5 w-screen flex flex-col">
          <ChatSection />
          <PlayBar src="/knowledgegraphs.mp3" />
        </section>
      </div>
    </main>
  );
}
