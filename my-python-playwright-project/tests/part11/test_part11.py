# ✅ Handle Hyper Links | Links in Playwright

def test_hyper_links(page):
    page.goto("https://the-internet.herokuapp.com/status_codes")
    page.click("text=200")
    assert "status_codes/200" in page.url
