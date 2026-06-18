# Virtual Environment Setup

This project uses a local virtual environment named `.venv`.

## Create the virtual environment (already done)

Run in the project root:

```bash
python3 -m venv .venv || python -m venv .venv
```

## Activate the environment

- On Linux/macOS (bash, zsh):

```bash
source .venv/bin/activate
```

- On Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

## Install requirements

After activation, install dependencies:

```bash
pip install -r requirements.txt
```

## Freeze current dependencies

To save installed packages into `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## Notes

- `.venv` is ignored by Git via `.gitignore`.
- If you need a different Python version, install it system-wide or use pyenv.
