from oscarcrab.llm import generate
"""
Core conversation logic for Oscar Crab.

This will eventually manage:
- LLM interaction (via Ollama or Transformers)
- Memory retrieval (vector DB)
- Personality injection
- Response generation
"""

class ChatAgent:
    """
    A simple talking agent with no memory (yet).

    Example:
        >>> agent = ChatAgent(name="Oscar")
        >>> agent.say("Hello!")
        'Hello! I am Oscar, your curious crab companion.'
    """
    def __init__(self, name: str = "Oscar", tone: str = "curious"):
        self.name = name
        self.tone = tone

    def say(self, message: str) -> str:
        prompt = f"{self.name} ({self.tone}) says: {message}"
        return generate(prompt)


def run_conversation_loop():
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