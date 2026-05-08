# 🚀 Deploy LLM & High-Performance Python Tooling

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An industrial-grade repository focused on Large Language Model (LLM) deployment and high-throughput Python systems. Designed for performance, scalability, and adherence to elite engineering standards.

---

## 🌟 Key Features

### 1. LLM Inference & Deployment
- **Efficient Templates**: Implementation of `AutoTokenizer.apply_chat_template` for optimized prompt engineering.
- **Optimized Loading**: Utilizing `torch_dtype="auto"` and `device_map="auto"` for maximum hardware utilization.
- **Production Ready**: Tested with Qwen and other state-of-the-art open-source models.

### 2. High-Performance Concurrency
- **Asyncio Mastery**: Demonstrated non-blocking I/O patterns using `httpx` with HTTP/2 support.
- **Thread Safety**: Robust `ThreadPoolExecutor` implementations for CPU-bound tasks.
- **Advanced Rate Limiting**: O(1) sliding window implementation using `collections.deque`.

---

## 📂 Project Roadmap

- [x] **Core LLM Inference**: Basic scripts for model generation.
- [x] **Concurrency Toolkit**: Reusable executors and rate limiters.
- [x] **Architecture Alignment**: Strict enforcement of `python-guide.md` conventions.
- [ ] **Web API Layer**: FastAPI integration for model-as-a-service.
- [ ] **Observability**: Structured JSON logging and OpenTelemetry integration.

---

## 🛠️ Usage

### 🚀 Inference Quick Start
```bash
python3 apply_chat_template.py
```

### ⚡ Concurrency Demo
```bash
python3 async_demo.py
```

---

## 📐 Design Philosophy

This project follows the **"Surgical Precision"** principle:
- **Minimize Abstraction**: Avoid deep inheritance or excessive design patterns.
- **Maximum Cohesion**: Logic is kept in tight, high-performance units.
- **Strict Typing**: 100% Type Hint coverage for safety and maintainability.
- **O(1) Redline**: Critical paths must maintain constant-time complexity.

---
**Maintainer:** [SongJin](https://github.com/AIMWLI)
