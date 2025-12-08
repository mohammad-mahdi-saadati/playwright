from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.p = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False, devtools=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def stop(self):
        pass
