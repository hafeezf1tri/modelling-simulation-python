# SimPy and Python Labs

This repository contains Python lab exercises for learning generators, basic scripting, and SimPy-based simulation work.


## Requirements

- Python 3.10 or newer
- pip
- SimPy, for simulation labs

Install SimPy directly with:

```bash
pip install simpy
```

Or install all project dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

If SimPy is not already listed in `requirements.txt`, add it:

```text
simpy
```

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Labs

Run any lab file with Python:
Example:
```bash
python lab6.py
```

To run the SimPy clinic simulation lab:

```bash
python lab8.py
```

## Lab Topics

The current lab files cover:

- Generator expressions
- Generator functions
- The `yield` keyword
- Iterating through generated values
- Simple task submissions using Python functions

Current SimPy labs include:

- Creating a simulation environment
- Modeling patient processes
- Using timeouts and events
- Simulating a doctor resource queue
- Showing patient arrival, consultation start, and clinic departure

## Example SimPy Program

```python
import simpy


def student(env, name):
    print(f"{name} starts studying at {env.now}")
    yield env.timeout(3)
    print(f"{name} finishes studying at {env.now}")


env = simpy.Environment()
env.process(student(env, "Student 1"))
env.run()
```

Run it with:

```bash
python filename.py
```

## Notes

- Keep each lab task in a separate file unless instructed otherwise.
- Use clear function names and readable output.
- Update `requirements.txt` when new packages are added.
