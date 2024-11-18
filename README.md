# playwrightPractice
Here is the README as one cohesive document:

---

# Pinterest Login Automation with Playwright

This repository contains a Python script that automates the login process for Pinterest using the [Playwright](https://playwright.dev/python/) framework. The script navigates to Pinterest's website, enters predefined credentials, and verifies the success of the login.

## Features

- **Automated Login**: Simulates a user logging into Pinterest using provided email and password.  
- **Element Verification**: Ensures the login button is hidden post-login, confirming a successful login attempt.  
- **Headless or Visual Execution**: Can be run with or without a GUI for debugging purposes.  

## Prerequisites

1. **Python**: Ensure Python 3.8 or newer is installed.  
2. **Playwright**: Install Playwright with the following command:
   ```bash
   pip install playwright
   ```
3. **Install Playwright Browsers**:  
   After installing Playwright, run the following to install the necessary browser binaries:
   ```bash
   playwright install
   ```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/pinterest-login-automation.git
   cd pinterest-login-automation
   ```

2. Update credentials:  
   Replace the placeholders for email and password in the script with your test credentials:
   ```python
   page.get_by_placeholder("Email").fill("your-email@example.com")
   page.get_by_placeholder("Password").fill("your-password")
   ```

3. Run the script:  
   Execute the script using:
   ```bash
   python pinterest_login.py
   ```

## Script Breakdown

1. **Navigate to Pinterest**:  
   The script directs the browser to Pinterest's homepage:
   ```python
   page.goto("https://www.pinterest.com/")
   ```

2. **Initiate Login**:  
   Clicks the login button:
   ```python
   page.locator("[data-test-id=\"simple-login-button\"]").get_by_role("button", name="Log in").click()
   ```

3. **Fill Credentials**:  
   Inputs the email and password:
   ```python
   page.get_by_placeholder("Email").fill("emailfortesting25@gmail.com")
   page.get_by_placeholder("Password").fill("emailfortesting25")
   ```

4. **Submit Login**:  
   Clicks the login button and verifies successful login:
   ```python
   page.locator("[data-test-id=\"registerFormSubmitButton\"]").get_by_role("button", name="Log in").click()
   expect(page.locator("[data-test-id=\"registerFormSubmitButton\"]").get_by_role("button", name="Log in")).to_be_hidden()
   ```

5. **Completion**:  
   Prints "Success" if the login process is verified.

## Notes

- **Security**: Avoid hardcoding sensitive credentials in the script. Use environment variables or a secure credentials manager.  
- **Headless Mode**: Set `headless=True` in `browser.launch()` for running in headless mode:
   ```python
   browser = playwright.chromium.launch(headless=True)
   ```
- **Error Handling**: Extend the script with exception handling for production use.

## Disclaimer

This script is intended for educational purposes and testing only. Ensure you comply with Pinterest's terms of service and avoid unauthorized or unethical usage.

## Contributing

Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the MIT License. 

--- 
