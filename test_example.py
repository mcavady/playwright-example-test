import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # ---start trace
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://jsmcavady.co.uk/")
    page.get_by_role("button", name="Accept").click()
    page.get_by_role("link", name="Shop", exact=True).click()
    page.get_by_role("heading", name="Blender3d").get_by_role("link").click()
    page.get_by_role("link", name="Industrial 3d Building Sale").click()
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_label("Remove Industrial 3d Building").click()
    expect(page.get_by_role("heading", name="Your cart is empty")).to_be_visible()
    expect(page.get_by_label("Your cart").get_by_role("heading")).to_contain_text("Your cart is empty")
    # ---endtrace
    context.tracing.stop(path = "trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
