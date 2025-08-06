from playwright.sync_api import sync_playwright, expect

def test_saucedemo_complete_flow_headed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=False makes the browser visible
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".inventory_item")).to_have_count(6)

        page.click("text=Add to cart", timeout=3000)
        page.click(".shopping_cart_link")
        page.click("text=Checkout")
        page.fill("#first-name", "Test")
        page.fill("#last-name", "User")
        page.fill("#postal-code", "12345")
        page.click("#continue")

        expect(page.locator(".summary_total_label")).to_contain_text("Total")
        page.click("#finish")
        expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

        browser.close()
