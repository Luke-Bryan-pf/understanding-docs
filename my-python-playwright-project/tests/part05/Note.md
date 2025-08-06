### Optional Notes  
📄 [tests/part05/notes.md](tests/part05/notes.md)

Covers:
- Running tests with `pytest` vs plain `python`
- Pros/cons of each approach
- Headless vs headed browser modes
- Summary comparison table

# Headless vs. Headed Mode
headless=True → Browser runs in background (default)
headless=False → Browser UI opens, good for debugging

Example:
browser = p.chromium.launch(headless=False)
-------
# Method 1: Using Pytest (Recommended)
Test functions must be named like test_*
No need to manually call test functions
Automatically discovers and runs tests

Great for:
Test reporting (PASSED/FAILED)
Scalability (many tests)
Integration with CI/CD


🔧 Run Command:
pytest test_example_pytest.py
-----
 # Method 2: Using Python Directly
You must call test functions inside a main() block
No built-in test report unless it fails

Good for:
Quick debugging
Running standalone scripts

🔧 Run Command:
python test_example_python.py

