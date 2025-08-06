
# Part 12: Handling Frames (Iframes)

Use `frame_locator` to target iframe content.

```python
frame = page.frame_locator("#frame_id")
frame.locator("selector").fill("text")
```

The test types inside the TinyMCE editor iframe.
---
What is an <iframe>?
An iframe is like a web page inside another web page.

Example:
Imagine a YouTube video embedded on a website — that video is loaded in an iframe.

So:
The main page is one document.
The iframe is a separate page embedded inside the main page.
To control or test stuff inside the iframe, you have to switch context to that inner frame.
