# JWKS Server – Project 1

Cristian Hernandez
EUID: ch0928
CSCE 3550 – Spring 2026

## Overview
This project implements a basic JWKS server using Python and FastAPI. The server generates RSA keys, assigns a kid and expiration time to each key, serves public keys at a JWKS endpoint, creates JWT tokens, and supports expired JWT tokens when requested. This project is for educational purposes.

## Setup Instructions
Create virtual environment:

```powershell
python -m venv venv
```

Activate virtual environment (Windows):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run Server

Start the server:

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

Server runs at: http://localhost:8080

## Test Endpoints

Open a second terminal.

Valid JWT:

```powershell
curl.exe -X POST http://localhost:8080/auth
```

JWKS endpoint:

```powershell
curl.exe http://localhost:8080/.well-known/jwks.json
```

Expired JWT:

```powershell
curl.exe -X POST "http://localhost:8080/auth?expired=true"
```

## Run Tests

```powershell
python -m pytest --cov=app --cov-report=term-missing
```

Coverage should be over 80%.

## Blackbox Testing

```powershell
.\gradebot.exe project-1 --run "uvicorn app.main:app --host 0.0.0.0 --port 8080"
```

This tests the server automatically.

## Project Structure

```
CyberP1/
|- app/
|   |-- keys.py
|   |-- main.py
|   |-- utils.py
|- tests/
|   |-- test_auth.py
|   |-- test_jwks.py
|- screenshots/
|   |-- blackbox.png
|   |-- coverage.png
|-- gradebox.exe
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Linting

Code has been formatted with `black` and linted with `pylint`.
Check code quality:
```powershell
pylint app/
black --check app/
```