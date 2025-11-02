"""
Unit tests for oscar.core
"""
import pytest
from oscarcrab import ChatAgent


def test_chat_agent_creation():
    agent = ChatAgent(name="Shellby")
    assert agent.name == "Shellby"
    assert agent.tone == "curious"


def test_chat_agent_say():
    agent = ChatAgent(name="Oscar")
    response = agent.say("Hi")
    assert "Hi" in response
    assert "Oscar" in response


def test_chat():
    # This is a stub. We'll test with mocks later
    assert True