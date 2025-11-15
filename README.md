#  Oscar-Core

This repository contains the core engine that powers Oscar Crab's conversation, memory, personality, and model management.

**Features (In Progress):**
- Persistent Memory: SQLite + embeddings for long-term recall
- Personality System: Customize Oscar's tone and behavior via `persona.json`
- Local AI Support: Integrates with Ollama and Transformers
- Emotion-Aware Responses: Coming soon!

**Project Links:**
- [Documentation](https://github.com/oscarcrab/oscar-docs)  
- [Oscar Crab Organization](https://github.com/oscarcrab)  

---

## Getting Started
**Setup**

```bash
git clone https://github.com/oscarcrab/oscar-core.git
cd oscar-core
pip install -e .
```

**Run the conversation loop**

From the command line Python REPL:

```bash
python -c "import oscarcrab; oscarcrab.chat()"
```

> **Note:** Make sure Ollama is running (other fallback backends to be implemented later).  
