import json
from oscarcrab.llm import OllamaBackend

def test_ollama_generate(monkeypatch):
    # Fake streaming response text
    fake_stream = "\n".join([
        json.dumps({"response": "Hello"}),
        json.dumps({"response": " world!"}),
    ])

    class FakeResponse:
        text = fake_stream
        def raise_for_status(self): pass

    def fake_post(url, json, timeout):
        return FakeResponse()

    monkeypatch.setattr("requests.post", fake_post)

    backend = OllamaBackend(model="dummy")
    result = backend.generate("Hi")

    assert result == "Hello world!"
