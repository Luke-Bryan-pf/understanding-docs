# POM Part 1 - Introduction and Folder Structure

## What is Page Object Model (POM)?
POM is a design pattern in automation testing that creates an object repository for web UI elements. It helps make tests more maintainable, reusable, and readable.

## Folder Structure Example
```
project/
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   └── test_login.py
├── notes/
│   └── notes.md
```
Each page is represented by a class that contains locators and related methods.