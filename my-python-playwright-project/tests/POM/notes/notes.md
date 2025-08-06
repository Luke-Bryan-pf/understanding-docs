
# Page Object Model (POM) - Final Refined Notes

## What is POM?
Page Object Model is a design pattern in Selenium and Playwright automation testing that creates an object repository for storing all web elements. Each page is represented by a separate class that contains locators and methods.

## Folder Structure Example

POM/
├── pages/
│   ├── base_page.py          ← Common shared methods like wait, click, etc.
│   └── login_page.py         ← Page class for login screen (locators + actions)
├── tests/
│   └── test_login.py         ← Test file calling the page methods
└── notes/
    └── notes.md              ← Description and explanation of each part

## BasePage
BasePage includes common methods like `visit()` and `get_title()` that can be reused by all other page classes.

## LoginPage
Contains:
- Locators for login fields and button
- A `login()` method to perform login
- Assertion methods to verify success/failure

## Tests
Tests use the page classes and avoid direct locator use.

### Real Site Used: https://practicetestautomation.com/practice-test-login/
- Username: `student`
- Password: `Password123`
-----------------------------
