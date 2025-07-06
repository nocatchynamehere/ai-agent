# 🔧 AI Code Assistant + Legacy Project Refactor

## ⚠️ Security Notice:
This tool executes local Python files. It includes safeguards against path traversal and enforces execution limits, but it should not be used to run untrusted code without additional sandboxing.

## 🧠 Project Summary

This project demonstrates the creation of a simple AI-powered command-line assistant using Google Gemini's API. The assistant accepts user prompts via terminal input and returns AI-generated content. As a practical application, we then use this AI tool to analyze and improve a legacy calculator codebase.

---

## 📦 Project Structure

```
.
├── .env                   # Environment variables (e.g., GEMINI_API_KEY)
├── main.py                # Entry point: CLI interface for AI interaction
├── tests.py               # Unit tests for get_files_info.py
├── calculator/            # Legacy calculator module (undergoing refactor)
│   ├── main.py            # Initial, unrefactored calculator logic
│   └── tests.py           # Unit tests for calculator functionality
│   └── pkg/               # Calculator submodules
│       ├── calculator.py  # Core calculation logic and functions
│       └── render.py      # Output rendering and formatting utilities
├── functions/             # Scripts to help the agent analyze files
│   └── get_files_info.py  # Output file info for working_directory
├── README.md              # Project overview and usage instructions
└── pyproject.toml         # Project metadata and dependencies
```

---

## 🚀 Part 1: AI Assistant – `agent.py`

This script sets up a lightweight terminal-based assistant using the Gemini 2.0 Flash model.

### ✅ Features
- CLI interface with `argparse` (coming soon)
- Optional `--verbose` flag for token usage info
- Loads API key securely via `.env`
- Sends prompt and receives response from Gemini API

### 🧪 Usage
```bash
uv run agent.py "What is the time complexity of bubble sort?"
uv run agent.py "Improve the following Python function..." --verbose
```

---

## 🛠️ Part 2: Calculator Refactor

The `calculator/main.py` file contains intentionally poor or incomplete code. We'll use the AI agent to:

1. Review the original code  
2. Identify and correct logic errors, poor design, or lack of features  
3. Create a cleaner, modular, and well-documented version  

---

## 🎯 Goals

- Practice integrating with an LLM (Large Language Model) API  
- Demonstrate prompt engineering for debugging and refactoring  
- Refactor legacy code into maintainable, readable components  
- Show AI's role as a **developer copilot**, not a magic solution  

---

## 🔐 .env File Example

```
GEMINI_API_KEY=your_api_key_here
```

---

## 📋 Requirements

Install dependencies with:

```bash
uv pip install
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

---

## 🧠 Attribution

Powered by [Google Gemini API](https://ai.google.dev). Project designed for educational use and developer skill-building.
