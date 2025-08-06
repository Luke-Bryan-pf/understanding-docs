# Playwright Pytest Demo Automation

This demo showcases comprehensive automation scenarios using Playwright with pytest, covering various real-world testing scenarios.

## Features Demonstrated

### Basic Automation
- ✅ Navigation and page assertions
- ✅ Form interactions (text inputs, dropdowns, checkboxes, radio buttons)
- ✅ Element interactions and waiting strategies
- ✅ Screenshot and video capture
- ✅ Error handling and retry mechanisms

### Advanced Features
- ✅ Mobile device emulation
- ✅ Keyboard and mouse actions
- ✅ Network request interception
- ✅ Multiple tab handling
- ✅ Data-driven testing
- ✅ Conditional testing logic

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers
```bash
playwright install
```

### 3. Verify Installation
```bash
playwright --version
pytest --version
```

## Running the Tests

### Run All Tests
```bash
pytest demo.py -v
```

### Run Specific Test Class
```bash
pytest demo.py::TestDemoAutomation -v
```

### Run Specific Test Method
```bash
pytest demo.py::TestDemoAutomation::test_basic_navigation_and_assertions -v
```

### Run with Different Options
```bash
# Run in headless mode
pytest demo.py --headless

# Run with slower execution (good for watching)
pytest demo.py --headed --slowmo=2000

# Run with parallel execution
pytest demo.py -n auto

# Generate HTML report
pytest demo.py --html=report.html --self-contained-html
```

## Test Structure

### TestDemoAutomation Class
Contains basic automation scenarios:
- `test_basic_navigation_and_assertions`: Basic page navigation and verification
- `test_form_interactions`: Complete form filling and submission
- `test_dynamic_content_handling`: Handling dynamic content and waiting
- `test_element_interactions`: Various element interaction patterns
- `test_screenshot_and_video_capture`: Screenshot and video recording
- `test_error_handling_and_retry`: Error handling and retry mechanisms
- `test_mobile_emulation`: Mobile device testing
- `test_keyboard_and_mouse_actions`: Keyboard and mouse interactions
- `test_network_interception`: Network request manipulation
- `test_multiple_tabs`: Multi-tab browser automation

### TestAdvancedDemo Class
Contains advanced scenarios:
- `test_data_driven_testing`: Data-driven testing approach
- `test_conditional_testing`: Conditional logic in automation

## Configuration

The `pytest.ini` file contains:
- Default test options (headed mode, slowmo, timeouts)
- Video and screenshot settings
- Test discovery patterns
- Custom markers for test categorization

## Best Practices Demonstrated

1. **Page Object Model Ready**: Structure supports easy conversion to POM
2. **Proper Waiting**: Uses appropriate wait strategies
3. **Error Handling**: Graceful error handling and recovery
4. **Assertions**: Comprehensive assertions using Playwright's expect
5. **Test Organization**: Logical grouping of related tests
6. **Documentation**: Clear docstrings and comments
7. **Configuration**: Externalized test configuration

## Troubleshooting

### Common Issues

1. **Browser not found**: Run `playwright install`
2. **Timeout errors**: Increase timeout in pytest.ini
3. **Element not found**: Check if page structure changed
4. **Network issues**: Verify internet connection

### Debug Mode
```bash
# Run with debug output
pytest demo.py -v -s --headed

# Run with Playwright debug
PWDEBUG=1 pytest demo.py
```

## Extending the Demo

This demo provides a foundation for:
- Adding more complex scenarios
- Implementing Page Object Model
- Adding API testing
- Integrating with CI/CD pipelines
- Adding custom fixtures and utilities

## Notes

- Tests use public test sites (example.com, httpbin.org)
- Screenshots are saved in the current directory
- Videos are saved in test-results/ directory
- All tests are designed to be independent and repeatable 