from playwright.sync_api import sync_playwright
def open_site(p, url: str = "https://danio.ir/"):
    browser = None
    context = None
    page = None
    try:
        browser = p.chromium.launch(
            headless=False,
            devtools=True   # باز شدن Inspect/DevTools
        )
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)

        print(f"✅ Opened site: {url}")
        return browser, context, page

    except Exception as e:
        print(f"❌ Failed to open site: {str(e)}")
        raise
