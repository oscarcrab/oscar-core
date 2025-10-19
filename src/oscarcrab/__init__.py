"""
Oscar Crab — A local-first AI companion.
"""
__version__ = "0.1.0"
__author__ = "Oscar Crab Team"

from oscarcrab.core import (
    ChatAgent,
    run_conversation_loop,
)

__all__ = [
    "ChatAgent",
    "run_conversation_loop",
]