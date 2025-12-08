from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.p = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.p = sync_playwright().start()

        self.browser = self.p.chromium.launch(
            headless=False,
            devtools=True   # DevTools باز می‌شود، ولی ما حالت موبایل را از این نمی‌گیریم
        )

        self.context = self.browser.new_context(
            viewport={"width": 375, "height": 812},   # آیفون
            device_scale_factor=3,
            is_mobile=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
                       "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        )

        self.page = self.context.new_page()
        self.page.goto("https://danio.ir")
        return self.page

    def stop(self):
        pass
