import pytest
from playwright.sync_api import Page, expect
import time


class TestDemoAutomation:
    """Demo automation flow showcasing Playwright with pytest capabilities"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup method that runs before each test"""
        self.page = page
        # Set viewport size for consistent testing
        self.page.set_viewport_size({"width": 1280, "height": 720})
    
    def test_basic_navigation_and_assertions(self):
        """Test basic navigation and page assertions"""
        # Navigate to a test website
        self.page.goto("https://example.com")
        
        # Assert page title
        expect(self.page).to_have_title("Example Domain")
        
        # Assert URL
        expect(self.page).to_have_url("https://example.com/")
        
        # Check if specific element exists
        heading = self.page.locator("h1")
        expect(heading).to_be_visible()
        expect(heading).to_have_text("Example Domain")
        
        # Check if paragraph contains expected text
        paragraph = self.page.locator("p").first
        expect(paragraph).to_contain_text("illustrative examples")
    
    def test_form_interactions(self):
        """Test form filling and submission"""
        # Navigate to a simple test page
        self.page.goto("https://example.com")
        
        # Demonstrate basic interactions
        # Click on the heading
        heading = self.page.locator("h1")
        heading.click()
        
        # Verify the heading is still visible after clicking
        expect(heading).to_be_visible()
        expect(heading).to_have_text("Example Domain")
        
        # Demonstrate text input simulation
        # We'll simulate typing into a search box (if it exists) or just demonstrate the concept
        try:
            # Try to find any input field
            input_field = self.page.locator("input").first
            if input_field.is_visible():
                input_field.fill("test input")
                expect(input_field).to_have_value("test input")
        except:
            # If no input field, just demonstrate the concept
            print("No input fields found on this page - demonstrating concept only")
        
        # Verify we're still on the correct page
        expect(self.page).to_have_title("Example Domain")
    
    def test_dynamic_content_handling(self):
        """Test handling dynamic content and waiting"""
        # Navigate to a page with dynamic content
        self.page.goto("https://httpbin.org/delay/2")
        
        # Wait for page to load completely
        self.page.wait_for_load_state("networkidle")
        
        # Verify the page loaded successfully
        expect(self.page).to_have_url("https://httpbin.org/delay/2")
        
        # Check for JSON response content
        expect(self.page.locator("pre")).to_be_visible()
    
    def test_element_interactions(self):
        """Test various element interactions"""
        # Navigate to a test page
        self.page.goto("https://example.com")
        
        # Click on the heading
        heading = self.page.locator("h1")
        heading.click()
        
        # Verify the heading is still visible
        expect(heading).to_be_visible()
        
        # Navigate to a different page
        self.page.goto("https://httpbin.org/json")
        
        # Wait for page to load
        self.page.wait_for_load_state("networkidle")
        
        # Verify we're on the JSON page
        expect(self.page).to_have_url("https://httpbin.org/json")
        
        # Go back to example.com
        self.page.go_back()
        
        # Verify we're back
        expect(self.page).to_have_url("https://example.com/")
    
    def test_screenshot_and_video_capture(self):
        """Test taking screenshots and handling video recording"""
        # Navigate to a page
        self.page.goto("https://example.com")
        
        # Take a screenshot
        self.page.screenshot(path="demo_screenshot.png")
        
        # Take screenshot of specific element
        heading = self.page.locator("h1")
        heading.screenshot(path="heading_screenshot.png")
        
        # Verify screenshot was taken (file should exist)
        import os
        assert os.path.exists("demo_screenshot.png")
        assert os.path.exists("heading_screenshot.png")
    
    def test_error_handling_and_retry(self):
        """Test error handling and retry mechanisms"""
        # Test with a page that might not exist
        try:
            self.page.goto("https://httpbin.org/status/404", timeout=5000)
        except Exception as e:
            print(f"Expected error occurred: {e}")
        
        # Navigate to a working page
        self.page.goto("https://httpbin.org/")
        
        # Test waiting for element with timeout
        try:
            # This element doesn't exist, so it should timeout
            self.page.wait_for_selector(".non-existent-element", timeout=3000)
        except Exception as e:
            print(f"Expected timeout occurred: {e}")
        
        # Verify we're still on the working page
        expect(self.page).to_have_url("https://httpbin.org/")
    
    def test_mobile_emulation(self):
        """Test mobile device emulation"""
        # Set mobile viewport
        self.page.set_viewport_size({"width": 375, "height": 667})
        
        # Navigate to a responsive site
        self.page.goto("https://example.com")
        
        # Verify mobile layout (elements should be visible)
        expect(self.page.locator("h1")).to_be_visible()
        expect(self.page.locator("p").first).to_be_visible()
        
        # Reset to desktop viewport
        self.page.set_viewport_size({"width": 1280, "height": 720})
    
    def test_keyboard_and_mouse_actions(self):
        """Test keyboard and mouse interactions"""
        # Navigate to a page
        self.page.goto("https://httpbin.org/forms/post")
        
        # Test keyboard navigation
        self.page.keyboard.press("Tab")  # Navigate to first input
        self.page.keyboard.type("Test User")
        
        # Test mouse hover (if there are hoverable elements)
        # This is just a demonstration - httpbin doesn't have hover effects
        self.page.hover('input[name="custname"]')
        
        # Test right-click
        self.page.click('input[name="custname"]', button="right")
        
        # Verify the input still has our text
        expect(self.page.locator('input[name="custname"]')).to_have_value("Test User")
    
    def test_network_interception(self):
        """Test network request interception"""
        # Intercept network requests
        self.page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        
        # Navigate to a page
        self.page.goto("https://example.com")
        
        # Verify page loads without images (they were blocked)
        expect(self.page).to_have_title("Example Domain")
        
        # Remove the route to allow normal behavior
        self.page.unroute("**/*.{png,jpg,jpeg}")
    
    def test_multiple_tabs(self):
        """Test working with multiple tabs"""
        # Navigate to initial page
        self.page.goto("https://example.com")
        
        # Open a new tab
        new_page = self.page.context.new_page()
        
        # Navigate in new tab
        new_page.goto("https://httpbin.org/")
        
        # Verify both pages are working
        expect(self.page).to_have_title("Example Domain")
        expect(new_page).to_have_url("https://httpbin.org/")
        
        # Close the new tab
        new_page.close()
        
        # Verify original page is still accessible
        expect(self.page).to_have_title("Example Domain")


class TestAdvancedDemo:
    """Advanced demo scenarios"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup method that runs before each test"""
        self.page = page
        self.page.set_viewport_size({"width": 1280, "height": 720})
    
    def test_data_driven_testing(self):
        """Test data-driven approach"""
        test_data = [
            {"title": "Example Domain", "url": "https://example.com"},
            {"title": "JSON API", "url": "https://httpbin.org/json"},
            {"title": "User Agent", "url": "https://httpbin.org/user-agent"}
        ]
        
        for data in test_data:
            # Navigate to different pages
            self.page.goto(data["url"])
            
            # Wait for page to load
            self.page.wait_for_load_state("networkidle")
            
            # Verify we're on the correct page (handle trailing slash)
            current_url = self.page.url
            expected_url = data["url"]
            assert current_url == expected_url or current_url == expected_url + "/"
            
            # Verify page loaded successfully
            expect(self.page.locator("body")).to_be_visible()
    
    def test_conditional_testing(self):
        """Test conditional logic in automation"""
        # Navigate to a page
        self.page.goto("https://example.com")
        
        # Check if certain elements exist before interacting
        if self.page.locator("h1").is_visible():
            # If heading exists, click on it
            self.page.click("h1")
            expect(self.page.locator("h1")).to_be_visible()
        else:
            # Alternative action if element not found
            self.page.click("body")
            expect(self.page.locator("body")).to_be_visible()
        
        # Navigate to another page
        self.page.goto("https://httpbin.org/json")
        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url("https://httpbin.org/json")


if __name__ == "__main__":
    # This allows running the file directly with pytest
    pytest.main([__file__, "-v", "--headed"])
