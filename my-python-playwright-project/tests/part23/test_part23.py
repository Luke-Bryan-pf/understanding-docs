# ✅ Maximize Browser | ViewPortSize | SetViewPortSize

def test_set_viewport(page):
    page.set_viewport_size({"width": 1280, "height": 800})
    page.goto("https://letcode.in")
    page.screenshot(path="viewport_test.png")