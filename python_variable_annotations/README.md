# Python - Variable Annotations

## Description

This project explores **type annotations** in Python 3, a feature that allows developers to explicitly declare the expected types of variables, function parameters, and return values. Type annotations improve code readability, enable static type checking with tools like `mypy`, and help catch bugs before runtime.

## Learning Objectives

At the end of this project, you should be able to explain:

- What type annotations are in Python 3
- How to use type annotations for functions and variables
- What duck typing is
- How to validate your code with `mypy`

## Requirements

- Python 3.9+
- All files start with `#!/usr/bin/env python3`
- All files end with a new line
- No external modules required (only `typing` from the standard library)

## Files

| File | Description |
|------|-------------|
| `0-add.py` | Annotated function that adds two floats and returns their sum |
| `1-concat.py` | Annotated function that concatenates two strings |
| `2-floor.py` | Annotated function that returns the floor of a float as an int |
| `3-to_str.py` | Annotated function that returns the string representation of a float |
| `4-define_variables.py` | Annotated variable definitions for `int`, `float`, `bool`, and `str` |
| `5-sum_list.py` | Annotated function that sums a list of floats |
| `6-sum_mixed_list.py` | Annotated function that sums a list of ints and floats |
| `7-to_kv.py` | Annotated function returning a tuple of a string and the square of a number |
| `8-make_multiplier.py` | Annotated function returning a multiplier function (Callable) |
| `9-element_length.py` | Duck-typed annotated function returning a list of (sequence, length) tuples |

## Key Concepts

### Basic Function Annotations

```python
def add(a: float, b: float) -> float:
    return a + b

print(add.__annotations__)
# {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```

### Variable Annotations

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### Complex Types with `typing`

```python
from typing import List, Union, Tuple, Callable, Iterable, Sequence

# List of floats
def sum_list(input_list: List[float]) -> float:
    return sum(input_list)

# Mixed list (int or float)
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))

# Tuple return type
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v ** 2))

# Callable return type
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier

# Duck typing with Iterable and Sequence
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

### Duck Typing

Duck typing means annotating based on **behavior** rather than a specific type. For example, `Iterable[Sequence]` accepts any object that is iterable and whose elements support `len()` — not just lists.

### Validating with `mypy`

```bash
pip install mypy
mypy 0-add.py
# Success: no issues found in 1 source file
```

## `typing` Module Reference

| Type | Usage |
|------|-------|
| `List[X]` | A list whose elements are of type `X` |
| `Union[X, Y]` | A value that can be either type `X` or `Y` |
| `Tuple[X, Y]` | A tuple with specific element types |
| `Callable[[X], Y]` | A function taking `X` and returning `Y` |
| `Iterable[X]` | Any iterable yielding elements of type `X` |
| `Sequence[X]` | Any sequence (supports `len` and indexing) |

## Author

This project is part of the **Holberton School Web Back End** curriculum.

## Repository

- **GitHub repository:** `holbertonschool-web_back_end`
- **Directory:** `python_variable_annotations`