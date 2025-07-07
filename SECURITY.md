# 🔐 Security Policy

## 📦 Project Scope: AI Code Assistant & Legacy Refactor

This project allows users to execute local Python files via a command-line AI assistant. To ensure safety, guardrails are in place to protect the executing environment from unintended or malicious behavior. However, **this project is not designed for running untrusted user input without additional sandboxing.**

---

## ✅ Current Security Features

### 1. **Path Traversal Protection**
- All file execution is restricted to a defined working directory.
- Attempting to access files outside this directory results in an error.

### 2. **File Type Filtering**
- Only files ending in `.py` are allowed to be executed.
- All other file types are rejected with a clear error message.

### 3. **Existence Verification**
- Files must exist and be readable.
- Execution is blocked if the file cannot be found.

### 4. **Timeout Enforcement**
- Each file execution is time-limited to 30 seconds.
- Prevents infinite loops or hanging processes.

### 5. **Output Isolation**
- `stdout` and `stderr` are captured and returned in formatted strings.
- No unfiltered console output or shell execution.

### 6. **No `shell=True` Usage**
- All subprocess execution avoids `shell=True`, protecting against shell injection attacks.

---

## ⚠️ Known Limitations

Even with guardrails, executing arbitrary Python code is inherently dangerous. This project does not include sandboxing or process isolation out-of-the-box.

---

## 🧪 Best Practices for Safe Use

| Scenario | Safe? | Recommendation |
|----------|-------|----------------|
| Running your own local `.py` scripts | ✅ Yes | Guardrails are sufficient |
| Allowing other developers on your team to run code | ⚠️ Yes | Ensure code is reviewed first |
| Executing arbitrary user-submitted code | ❌ No | Add sandboxing (e.g., Docker) |
| Deploying as a public-facing API | ❌ No | Add authentication, sandboxing, and rate limits |

---

## 📄 Reporting Vulnerabilities

If you discover a security issue or exploit path, please open a GitHub issue using the security label or contact the maintainer privately.

---

## 🔐 License and Responsibility

This code is provided for educational and personal use. The maintainers are **not responsible** for any damage, data loss, or unintended effects caused by unsafe execution or misuse of this tool.

Use responsibly.