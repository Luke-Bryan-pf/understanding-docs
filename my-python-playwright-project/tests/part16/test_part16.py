# ✅ Selecting elements that contain other elements

def test_nested_frames(page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    # Get the top frame first
    top_frame = page.frame(name="frame-top")

    # Then find the left frame inside the top frame
    left_frame = next(f for f in top_frame.child_frames if f.name == "frame-left")

    # Assert the text inside the left frame
    assert "LEFT" in left_frame.inner_text("body")




#Correct frame navigation: You cannot access elements inside frames directly from the main page; you must switch into them.
#Nested frame handling: It first targets the outer frame, then drills down.
#Text validation: It checks the actual page content inside that frame.

