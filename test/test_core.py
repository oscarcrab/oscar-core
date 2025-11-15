"""
Unit tests for oscar.core
"""
import pytest
from oscarcrab import ChatAgent


def test_chat_agent_creation():
    agent = ChatAgent(name="Shellby")
    assert agent.name == "Shellby"
    assert agent.tone == "curious"


def test_chat_agent_say(monkeypatch):
    # Mock the LLM call so it doesn't hit Ollama
    def fake_generate(prompt):
        return "Hi there! I am Oscar the crab."

    monkeypatch.setattr("oscarcrab.core.generate", fake_generate)

    agent = ChatAgent(name="Oscar")
    response = agent.say("Hi")

    assert "Hi" in response
    assert "Oscar" in agent.name
    assert isinstance(response, str)


def test_chat():
    # This is a stub. We'll test with mocks later
    assert True