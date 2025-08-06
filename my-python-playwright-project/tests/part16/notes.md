
# Part 16: Selecting Elements that Contain Other Elements

## Definition
This technique is used to locate an element **inside another container** — for example, inside a frame, table, or nested component.

## Example Use Case:
You want to interact with an element **within a frame** or section.

## Playwright Approach:
Use `.frame_locator()` or `.locator()` within the parent element.

This test navigates nested iframes and asserts inner text of the left frame.
---
Topic Summary:
This part covers how to select parent elements that contain specific child elements using Playwright locators. This is useful when you can’t directly access a specific element, but you know the structure or inner content.

Example:
page.locator("div:has(span.text-success)")
div:has(span.text-success) → Selects any <div> that contains a <span> with class text-success.

Why it's useful:
Helps in navigating nested DOM structures where parent-child relationships are important.

Useful when testing UI components that render dynamic child elements.
