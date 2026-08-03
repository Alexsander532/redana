"""Tira screenshot da home e da hero em viewport 1440x900."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
    page = ctx.new_page()
    page.goto("http://localhost:8765/", wait_until="networkidle")
    page.wait_for_timeout(500)
    # Screenshot da hero (primeira dobra + um pouco)
    page.screenshot(path="imagens/hero/screenshot_viewport.png", full_page=False)
    # Screenshot da página inteira
    page.screenshot(path="imagens/hero/screenshot_full.png", full_page=True)
    print("ok")
    browser.close()
