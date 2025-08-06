# tests/part01/test_intro.py
# 🔹 Python Playwright Beginner [2023] Part 1: Introduction to Playwright

# Summary:
# Playwright is a Node.js/Python/Java/.NET library for browser automation.
# Supports Chromium, Firefox, and WebKit.
# Enables fast, reliable testing with features like auto-waiting, tracing, and debugging.
# Ideal for end-to-end UI test automation.

from playwright.sync_api import sync_playwright

def test_open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False opens browser
        page = browser.new_page()
        page.goto("https://example.com")
        print(page.title())
        browser.close()