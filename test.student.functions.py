from functions import detect_and_report_bug


# ------------------------------
# 1. باز کردن سایت
# ------------------------------

def open_site(p, url: str = "https://danio.ir/"):
    """
    باز کردن سایت با Playwright.
    در صورت خطا: با detect_and_report_bug اسکرین‌شات و گزارش می‌گیرد.
    """
    browser = None
    context = None
    page = None
    try:
        browser = p.chromium.launch(
            headless=False,
            devtools=True   # ← این‌جاست، اینسپکت همیشه موقع باز شدن روشن می‌شود
        )
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(2000)
        print(f"✅ Opened site: {url}")

        bug = detect_and_report_bug(
            page,
            chapter="system",
            skill="open_site",
            stage="after_open",
            require_submit_visible=False
        )
        if bug:
            raise Exception(f"Site open detected bug: {bug}")

        return browser, context, page

    except Exception as e:
        print(f"❌ Failed to open site: {str(e)}")
        if page:
            detect_and_report_bug(
                page,
                chapter="system",
                skill="open_site",
                stage="exception"
            )
        if browser:
            browser.close()
        raise
  


# ------------------------------
# 2. لاگین
# ------------------------------

def login(page, username: str = "danesh_t1", password: str = "danesh_t1"):
    """
    پر کردن فرم لاگین و ورود به سایت.
    در صورت خطا یا ارور 500 → detect_and_report_bug.
    """
    try:
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_timeout(2000)

        # بررسی کنیم آیا خطا یا ارور 500 ظاهر شده؟
        bug = detect_and_report_bug(
            page,
            chapter="system",
            skill="login",
            stage="after_submit"
        )
        if bug:
            raise Exception(f"Login detected bug: {bug}")

        print(f"✅ Logged in as {username}")

    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        detect_and_report_bug(
            page,
            chapter="system",
            skill="login",
            stage="exception"
        )
        raise