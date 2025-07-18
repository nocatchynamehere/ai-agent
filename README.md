# 🤖 AI-Powered Code Assistant & Legacy Refactor Project

## ⚠️ **Security Notice:**  
This tool includes guardrails such as path whitelisting and a 30-second execution timeout. However, it does execute local Python files and **must not** be used with untrusted or user-submitted code unless further sandboxing (e.g., containers, firejailing) is added.

## 🧠 Project Summary

This is a two-part educational project that demonstrates:

1. How to build a secure, CLI-based AI assistant using the Gemini API  
2. How to use that assistant to review and refactor a poorly written legacy Python module (calculator)

The result is a powerful example of AI-assisted software engineering — blending prompt design, code analysis, and Python tooling.

---

## 📦 Project Structure

```
.
├── .env                     # Environment variables (e.g., GEMINI_API_KEY)
├── calculator/              # Legacy calculator module (undergoing refactor)
│   ├── lorem.txt            # Used to test truncate, must have at least 10000 chars
│   ├── main.py              # Initial, unrefactored calculator logic
│   ├── morelorem.txt        # Generated by function tests
│   ├── pkg/                 # Calculator submodules
│   │   ├── calculator.py    # Core calculation logic and functions
│   │   └── render.py        # Output rendering and formatting utilities
│   └── tests.py             # Unit tests for calculator functionality
├── functions/               # Holds reusable utility logic (file I/O, execution control)
│   ├── call_function.py     # Executes functions for the agent
│   ├── get_file_content.py  # Gets file statistics
│   ├── get_files_info.py    # Reads file and truncates
│   ├── write_file.py        # Writes to file
│   └── run_python_file.py   # Guardrails for running python files
├── main.py                  # Entry point: CLI interface for AI interaction
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Project overview and usage instructions
├── SECURITY.md              # Project security features and warnings
├── tests.py                 # Unit tests for functions
└── uv.lock                  # Project dependency lockfile
```

---

## 🚀 Part 1: AI Assistant – `main.py`

This script sets up a lightweight terminal-based assistant using the Gemini 2.0 Flash model.

## ✅ Features

- Terminal-based AI assistant using Gemini 2.0 Flash
- Secure `.env` API key loading
- Guarded file execution via `run_python_file.py` with:
  - Path traversal protection
  - Extension filtering
  - Execution timeouts
- Output formatting (stdout/stderr/result codes)
- Works with `uv` and `pyproject.toml` for dependency isolation

### 🧪 Usage
```bash
uv run agent.py "What is the time complexity of bubble sort?"
# Will give a flat out response or time out

uv run agent.py "Improve the following Python function..." --verbose
# Will include information on what the AI-agent is doing
```

---

## 🛠️ Part 2: Calculator Refactor

The `calculator/main.py` file contains intentionally poor or incomplete code. We'll use the AI agent to:

1. Review the original code  
2. Identify and correct logic bugs, poor structure, and missing features
3. Create a cleaner, modular, and well-documented version  

---

## 🎯 Goals

- Practice integrating with an LLM (Large Language Model) API  
- Demonstrate prompt engineering for debugging and refactoring  
- Refactor legacy code into maintainable, readable components  
- Show AI's role as a **developer copilot**, not a magic solution  

---

## 🔐 .env File Example

This file is required - main.py will exit if GEMINI_API_KEY is missing.
```
GEMINI_API_KEY=your_api_key_here
```

---

## 📋 Requirements

Install dependencies with:

```bash
uv sync
```

Contents:
```
python-dotenv
google-generativeai
```

---

## 📈 Future Improvements

- Add support for code streaming or multiline responses  
- Interactive loop mode (like a chatbot shell)  
- Load code directly into the AI prompt from file  
- Add logging or output-to-file options
- Allow the AI to summarize changes it made after tool use
- Support writing diffs instead of full overwrites  

---

## 🧠 Attribution

Powered by [Google Gemini API](https://ai.google.dev). Project designed for educational use and developer skill-building.
