🔹 Python Playwright Beginner [2023] Part 3: Install and Setup Playwright | Python

# 1. Create a virtual environment
python -m venv venv

# 2. Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install required packages
pip install pytest playwright

# 4. Install browser binaries
playwright install

-----------

## Part 3 - Install & Setup Playwright

### Steps to Setup
1. Create virtual environment
2. Install Playwright and Pytest
3. Install supported browsers (`playwright install`)
4. Validate installation with a simple test

### Test:
- Launches Chromium headlessly
- Navigates to https://playwright.dev/python
- Asserts the page title contains "Playwright"

