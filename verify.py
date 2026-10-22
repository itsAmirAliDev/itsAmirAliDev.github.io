from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")

    # Wait for the fade-in animation and some typing effect to happen
    page.wait_for_timeout(3000)

    # Hover over a social button to see the glow/slide effect
    page.locator(".btn-yt").first.hover()
    page.wait_for_timeout(1000)

    # Take screenshot at the key moment showing the hover state and glassmorphism
    page.screenshot(path="/home/jules/verification/screenshots/verification2.png")

    # Wait longer to capture more of the typing and floating animation for the video
    page.wait_for_timeout(4000)

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