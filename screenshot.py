from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 2000})
    page.goto('http://localhost:8000')
    page.screenshot(path='screenshot.png', full_page=True)
    browser.close()
