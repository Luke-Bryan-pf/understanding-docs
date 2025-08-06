# ✅ TraceViewer | Capture Page Actions, Screenshot, Network Call

def test_trace_capture(page, context):
    context.tracing.start(screenshots=True, snapshots=True)
    page.goto("https://example.com")
    page.click("text=More information")
    context.tracing.stop(path="trace.zip")


# to view : playwright show-trace trace.zip