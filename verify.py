from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    # This is a static file, so we can use file://
    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")
    page.wait_for_timeout(500)

    # Hover over the card to see the effect
    page.locator(".container").hover()
    page.wait_for_timeout(500)

    # Hover over a social button to see the effect
    page.locator(".btn-yt").first.hover()
    page.wait_for_timeout(500)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()