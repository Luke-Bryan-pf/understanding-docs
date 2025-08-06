# POM Part 5 - Adding Assertions to Page Class

Added two assertion methods to `LoginPage`:
- `assert_login_successful()` checks for success message
- `assert_login_failed()` checks for error message

This keeps test code clean and puts assertions inside page class.