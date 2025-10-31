import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
from abc import ABC, abstractmethod
from pathlib import Path
import yaml

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
        model = model or CONFIG["model"]["ollama"]
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        try:
            r = requests.post(self.url, json={"model": self.model, "prompt": prompt}, timeout=30)
            r.raise_for_status()
            # Ollama streams lines of JSON — we take the last completed text
            lines = [line for line in r.text.splitlines() if line.strip()]
            return lines[-1] if lines else "(no response)"
        except Exception:
            raise RuntimeError("Ollama backend unavailable.")


class TransformersBackend(LLMBackend):
    """Fallback backend using Hugging Face Transformers."""

    def __init__(self, model_name: str = None):
        model_name = model_name or CONFIG["model"]["transformers"]
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=128)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


def load_backend() -> LLMBackend:
    """Try Ollama first; fallback to Transformers."""
    try:
        requests.get("http://localhost:11434", timeout=1)
        return OllamaBackend()
    except Exception:
        return TransformersBackend()


# Singleton instance
_backend = load_backend()

def generate(prompt: str) -> str:
    """Unified entrypoint for text generation."""
    return _backend.generate(prompt)
