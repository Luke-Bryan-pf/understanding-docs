# Project Structure
# .
# ├── main.py
# ├── requirements.txt
# └── README.md

# main.py
# test_google.py
def test_google_homepage(page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()


# requirements.txt
# (Add your dependencies here, e.g. flask, requests)

# README.md
# New Python Project
