# New Python Playwright Project

## Overview
This project is a Python application that integrates Playwright for browser automation. It serves as a template for building and testing web applications.

## Project Structure
```
my-python-playwright-project
├── main.py
├── tests
│   └── test_playwright.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd my-python-playwright-project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main application, execute:
```bash
python main.py
```

## Running Tests

To execute the Playwright tests, run:
```bash
pytest tests/test_playwright.py
```

## Dependencies

This project uses the following libraries:
- Playwright
- pytest (for testing)

Make sure to check `requirements.txt` for the complete list of dependencies.