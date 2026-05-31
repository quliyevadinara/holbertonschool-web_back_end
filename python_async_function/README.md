# Python Async Functions

A set of Python modules exploring asynchronous programming with `asyncio` — covering coroutines, concurrent execution, runtime measurement, and `asyncio.Task` objects.

---

## Setup

```bash
chmod +x 0-basic_async_syntax.py
chmod +x 1-concurrent_coroutines.py
chmod +x 2-measure_runtime.py
chmod +x 3-tasks.py
chmod +x 4-tasks.py
```

Or all at once:

```bash
chmod +x *.py
```

---

## Files

### 0. `0-basic_async_syntax.py` — Basic Async Coroutine

Defines `wait_random(max_delay=10)`, an async coroutine that waits a random float number of seconds between `0` and `max_delay`, then returns that delay.

```python
async def wait_random(max_delay: int = 10) -> float:
```

**Usage:**

```bash
./0-main.py
# 9.034261504534394
# 1.6216525464615306
# 10.634589756751769
```

---

### 1. `1-concurrent_coroutines.py` — Concurrent Coroutines

Defines `wait_n(n, max_delay)`, which spawns `wait_random` `n` times concurrently using `asyncio.gather()` and returns all delays in ascending order — without using `sort()`.

```python
async def wait_n(n: int, max_delay: int) -> List[float]:
```

**Usage:**

```bash
./1-main.py
# [0.96, 1.02, 1.79, 3.64, 4.50]
# [0.07, 1.51, 3.35, 3.70, 3.77, 4.74, 5.50, 5.75, 6.10, 6.83]
# [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

---

### 2. `2-measure_runtime.py` — Measure Runtime

Defines `measure_time(n, max_delay)`, a regular (non-async) function that times a full run of `wait_n(n, max_delay)` and returns the average time per coroutine (`total_time / n`).

```python
def measure_time(n: int, max_delay: int) -> float:
```

**Usage:**

```bash
./2-main.py
# 1.759705400466919
```

---

### 3. `3-tasks.py` — asyncio.Task

Defines `task_wait_random(max_delay)`, a regular (non-async) function that wraps `wait_random` in an `asyncio.Task` and returns it.

```python
def task_wait_random(max_delay: int) -> asyncio.Task:
```

**Usage:**

```bash
./3-main.py
# <class '_asyncio.Task'>
```

---

### 4. `4-tasks.py` — task_wait_n

Defines `task_wait_n(n, max_delay)`, which mirrors `wait_n` but uses `task_wait_random` instead of `wait_random` directly. Returns delays in ascending order.

```python
async def task_wait_n(n: int, max_delay: int) -> List[float]:
```

**Usage:**

```bash
./4-main.py
# [0.22, 1.19, 1.84, 2.14, 4.00]
```

---

## Concepts Covered

| Concept                          | Where used                                 |
| -------------------------------- | ------------------------------------------ |
| `async`/`await` syntax           | All files                                  |
| `asyncio.sleep()`                | `0-basic_async_syntax.py`                  |
| `asyncio.gather()`               | `1-concurrent_coroutines.py`, `4-tasks.py` |
| `time.perf_counter()`            | `2-measure_runtime.py`                     |
| `asyncio.Task`                   | `3-tasks.py`, `4-tasks.py`                 |
| In-order insertion (no `sort()`) | `1-concurrent_coroutines.py`, `4-tasks.py` |

---

## Requirements

- Python 3.7+
- No external dependencies (stdlib only: `asyncio`, `random`, `time`)

---

## Repository

- **GitHub:** `holbertonschool-web_back_end`
- **Directory:** `python_async_function`
