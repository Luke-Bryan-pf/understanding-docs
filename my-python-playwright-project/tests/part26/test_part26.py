# ✅ JavaScript pop ups | Alert | Confirm | Prompt dialog box
import time
from playwright.sync_api import Page

def test_all_alerts(page: Page):
    page.goto("https://demoqa.com/alerts", timeout=60000)
    page.evaluate("window.scrollBy(0, 600)")
    time.sleep(1)

    # Simple alert
    page.once("dialog", lambda dialog: (print("Simple alert:", dialog.message), dialog.accept()))
    page.click("#alertButton")
    time.sleep(1)

    # Delayed alert
    page.once("dialog", lambda dialog: (print("Timer alert:", dialog.message), dialog.accept()))
    page.click("#timerAlertButton")
    time.sleep(6)  # wait for alert to appear

    #  Confirm alert (OK/Cancel)
    def handle_confirm(dialog):
        print("Confirm alert:", dialog.message)
        dialog.accept()  # or dialog.dismiss()

    page.once("dialog", handle_confirm)
    page.click("#confirmButton")
    time.sleep(1)

    # Prompt alert (text input)
    def handle_prompt(dialog):
        print("Prompt alert:", dialog.message)
        dialog.accept("Test")  

    page.once("dialog", handle_prompt)
    page.click("#promtButton")
    time.sleep(2)
