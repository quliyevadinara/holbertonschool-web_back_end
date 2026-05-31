# Python Async Comprehension

A set of Python modules exploring async generators, async comprehensions, and parallel coroutine execution with `asyncio`.

---

## Setup

```bash
chmod +x 0-async_generator.py
chmod +x 1-async_comprehension.py
chmod +x 2-measure_runtime.py

# or all at once:
chmod +x *.py
```

---

## Files

### 0. `0-async_generator.py` — Async Generator

Defines `async_generator()`, an async coroutine that loops 10 times. Each iteration waits 1 second asynchronously, then yields a random float between 0 and 10.

```python
async def async_generator() -> Generator[float, None, None]:
```

**Usage:**

```bash
./0-main.py
# [4.40, 6.90, 6.29, 4.54, 4.13, 9.99, 6.72, 9.84, 1.00, 1.37]
```

---

### 1. `1-async_comprehension.py` — Async Comprehension

Defines `async_comprehension()`, which collects 10 random floats from `async_generator` using a single async comprehension and returns them as a list.

```python
async def async_comprehension() -> List[float]:
```

**Usage:**

```bash
./1-main.py
# [9.86, 8.57, 1.74, 4.07, 0.55, 8.08, 8.38, 1.54, 7.71, 7.67]
```

---

### 2. `2-measure_runtime.py` — Parallel Runtime Measurement

Defines `measure_runtime()`, which runs `async_comprehension` four times **in parallel** using `asyncio.gather` and returns the total wall-clock time elapsed.

```python
async def measure_runtime() -> float:
```

**Usage:**

```bash
./2-main.py
# 10.021936893463135
```

#### Why ~10 seconds and not ~40?

Each `async_comprehension` call takes ~10 seconds (10 yields × 1 second sleep each). Running four of them **sequentially** would take ~40 seconds. But `asyncio.gather` launches all four **concurrently** — while one coroutine is `await`-ing `asyncio.sleep(1)`, the event loop switches to the others. Since all four sleep periods **overlap**, the total wall-clock time equals the duration of the longest coroutine (~10s), not their sum (~40s).

```
Sequential:  [--10s--][--10s--][--10s--][--10s--]  → ~40s
Parallel:    [--10s--]                              → ~10s
             [--10s--]
             [--10s--]
             [--10s--]
```

---

## Concepts Covered

| Concept                                 | Where used                 |
| --------------------------------------- | -------------------------- |
| `async def` + `yield` (async generator) | `0-async_generator.py`     |
| `await asyncio.sleep()`                 | `0-async_generator.py`     |
| `async for` in comprehension            | `1-async_comprehension.py` |
| `asyncio.gather()` for parallelism      | `2-measure_runtime.py`     |
| `time.perf_counter()` for timing        | `2-measure_runtime.py`     |

---

## Requirements

- Python 3.7+
- No external dependencies (stdlib only: `asyncio`, `random`, `time`)

---

## Repository

- **GitHub:** `holbertonschool-web_back_end`
- **Directory:** `python_async_comprehension`
