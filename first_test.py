import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.pinterest.com/")
    page.wait_for_load_state("networkidle")
    page.locator("[data-test-id=\"simple-login-button\"]").get_by_role("button", name="Log in").click()
    page.get_by_placeholder("Email").fill("emailfortesting25@gmail.com")
    page.get_by_placeholder("Email").press("Tab")
    page.get_by_placeholder("Password").fill("emailfortesting25")
    page.locator("[data-test-id=\"registerFormSubmitButton\"]").get_by_role("button", name="Log in").click()
    expect(page.locator("[data-test-id=\"registerFormSubmitButton\"]").get_by_role("button", name="Log in")).to_be_hidden()
    print("Success")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
