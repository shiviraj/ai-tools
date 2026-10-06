# Agentic AI for Beginners

A beginner-friendly project to learn **LLMs, LangChain, Tools, Agents, RAG, and Agentic AI** using local/open-source models.

This project uses **Ollama** to run LLMs locally on your machine, so the application does not require an OpenAI API key or paid LLM API calls.

---

## 1. Prerequisites

Make sure the following are installed:

- macOS
- Python 3.14+
- Homebrew
- Ollama
- Git
- VS Code (recommended)

Check Python:

```bash
python3 --version
```

Check Homebrew:

```bash
brew --version
```

---

# 2. Project Setup

Clone the project 

Create a Python virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Verify:

```bash
which python3
python3 --version
```

You should see a path similar to:

```text
.../agentic-ai/.venv/bin/python
```

---

# 3. Install Python Dependencies

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

---

# 4. Ollama

Ollama allows us to run LLMs locally.

Official website:

https://ollama.com/

## Install Ollama

Using Homebrew:

```bash
brew install --cask ollama
```

Verify installation:

```bash
ollama --version
```

---

# 5. Start Ollama

Start the Ollama server:

```bash
ollama serve
```

Keep this terminal running.

Ollama runs locally and exposes its API by default at:

```text
http://localhost:11434
```

You can verify that Ollama is running:

```bash
curl http://localhost:11434
```

---

# 6. Download an LLM

For this project we use:

```text
llama3.2
```

Download it:

```bash
ollama pull llama3.2
```

Check installed models:

```bash
ollama list
```

You should see something similar to:

```text
NAME       ID       SIZE
llama3.2   ...      ...
```

---

# 7. Test Ollama

Before connecting LangChain, test the model directly:

```bash
ollama run llama3.2
```

Then ask:

```text
What is the capital of India?
```

Expected response:

```text
New Delhi
```

Exit the model:

```text
/bye
```

---


This project is the foundation for that goal.