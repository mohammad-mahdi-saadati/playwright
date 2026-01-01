from playwright.sync_api import sync_playwright, TimeoutError

class BrowserManager:
    def __init__(self):
        self.p = None
        self.browser = None
        self.context = None
        self.page = None
    def start(self):
        try:
            self.p = sync_playwright().start()
            self.browser = self.p.chromium.launch(
                headless=False,
                args=["--window-size=375,812"],
                devtools=False 
            )
            self.context = self.browser.new_context(
                viewport={"width": 375, "height": 812},
                device_scale_factor=3,
                is_mobile=True,
                user_agent=(
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
                )
            )
            self.page = self.context.new_page()
            self.page.goto("https://www.eduland.ir/auth/login", timeout=30000)
            try:
                self.page.wait_for_load_state("load", timeout=10000)
            except TimeoutError:
                self.page.wait_for_load_state("domcontentloaded", timeout=5000)
            try:
                ua = self.page.evaluate("navigator.userAgent")
                w = self.page.evaluate("window.innerWidth")
                h = self.page.evaluate("window.innerHeight")
                print("=== MOBILE EMULATION INFO ===")
                print("UA:", ua)
                print("INNER WIDTH:", w)
                print("INNER HEIGHT:", h)
                print("==============================")
            except Exception as e:
                print("Couldn't evaluate page properties:", e)
            return self.page
        except Exception as e:
            print("Browser start failed:", str(e))
            self.stop()
            raise
    def stop(self):
        try:
            if self.context:
                self.context.close()
                self.context = None
            if self.browser:
                self.browser.close()
                self.browser = None
            if self.p:
                self.p.stop()
                self.p = None
        except Exception:
            pass
