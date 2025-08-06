# ✅ Handle Frames | Iframes in Playwright
def test_handle_iframe(page):
    page.goto("https://the-internet.herokuapp.com/iframe")
    frame = page.frame_locator("#mce_0_ifr")
    frame.locator("body").evaluate("node => node.innerHTML = 'Hello from Playwright!'")
    # Now assert that the content is correctly set
    assert frame.locator("body").text_content().strip() == "Hello from Playwright!"
