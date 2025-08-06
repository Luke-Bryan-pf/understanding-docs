
# Part 07: Trace Viewer

Learn how to capture and visualize test execution with Playwright's `tracing` feature.

## Key Commands
```python
context.tracing.start(screenshots=True, snapshots=True)
...
context.tracing.stop(path="trace.zip")
```

Then view it with:
```bash
playwright show-trace trace.zip
```
