# Robot Status — Finite State Machine (FSM)

A small Python project to **model a robot/device status** using a **finite state machine (FSM)**: `OFF → ON → ERROR → RESET`.  
The goal is to provide a clean, testable base that can later be extended to real-world cases (e.g., Doosan/UR robots, I/O signals, watchdogs, etc.).

> **Repository structure**
>
> - `app/` — FSM source code  
> - `tests/` — unit tests with `pytest`  
> - `requirements.txt` — minimal dependencies  
> - `.gitignore` — standard Python ignores
>
> _(see the full tree in the repo)_.

---

## Objectives

- Implement a clean, readable FSM (`OFF`, `ON`, `ERROR`, `RESET`).
- Validate transitions through **unit tests** (`pytest`).
- Provide a skeleton ready for integration with real robot status logic (connection, heartbeat, error detection).

---

##  Requirements

- Python **3.10+** (recommended)
- `pytest` as test runner

Install dependencies:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
