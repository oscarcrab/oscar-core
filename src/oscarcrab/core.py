from oscarcrab.llm import generate
"""
Core conversation logic for Oscar Crab.

This will eventually manage:
- LLM interaction (via Ollama)
- Memory retrieval (vector DB)
- Personality injection
- Response generation
"""

class ChatAgent:
    def __init__(self, name: str = "Oscar", tone: str = "curious"):
        self.name = name
        self.tone = tone
        # System prompt: tells the LLM who the agent is
        self.system_prompt = (
            f"You are a virtual AI crab named {self.name}. "
            f"Your tone is {self.tone}. "
            "Answer as the crab would."
        )

    def say(self, message: str) -> str:
        # Include the system context plus user input
        prompt = f"{self.system_prompt}\nHuman: {message}\nCrab:"
        return generate(prompt)


def chat():
    """Start a simple CLI loop (stub for future UI)."""
    agent = ChatAgent()
    print(f"{agent.name} is ready! Type 'quit' to exit.")
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() in {"quit"}:
                print("See you later!")
                break
            response = agent.say(user_input)
            print(f"🦀 {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break