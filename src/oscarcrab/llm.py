import requests
from abc import ABC, abstractmethod
from pathlib import Path
import yaml
import json

def load_config():
    """Load package-level config.yaml from the same directory."""
    config_path = Path(__file__).parent / "config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"Missing config.yaml at {config_path}")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

class LLMBackend(ABC):
    """Abstract backend interface."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a text completion."""
        pass


class OllamaBackend(LLMBackend):
    """Interact with local Ollama server."""

    def __init__(self, model: str = None):
        self.model = model or CONFIG["model"]["ollama"]
        self.server_url = CONFIG["ollama"].get("server_url")
        self.timeout = CONFIG["ollama"].get("timeout")
        self.max_tokens = CONFIG["generation"].get("max_tokens")
        self.temperature = CONFIG["generation"].get("temperature")

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature
        }
        try:
            r = requests.post(self.server_url + "/api/generate", json=payload, timeout=self.timeout)
            r.raise_for_status()
            response_text = ""
            for i, line in enumerate(r.text.splitlines()):
                try:
                    data = json.loads(line)
                    if "response" in data:
                        response_text += data["response"]
                except json.JSONDecodeError:
                    continue
            return response_text or "(no response)"
        except Exception as e:
            raise RuntimeError(f"Ollama backend unavailable: {e}")


def load_backend() -> LLMBackend:
    """Try Ollama first, fallback to other backends later."""
    try:
        requests.get("http://localhost:11434", timeout=1)
        return OllamaBackend()
    except Exception:
        raise RuntimeError("No LLM backend available.")


# Singleton instance
_backend = load_backend()

def generate(prompt: str) -> str:
    """Unified entrypoint for text generation."""
    return _backend.generate(prompt)
