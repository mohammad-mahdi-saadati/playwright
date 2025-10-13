import os, re, datetime
from typing import List, Tuple
from playwright.sync_api import sync_playwright
import pandas as pd


def detect_and_report_bug(page, stage: str = "", verbose: bool = True) -> str | None:
    """بررسی خطاهای مهم هنگام لاگین و باز کردن صفحه."""
    tag = None

    try:
        if page.locator("text=500 Internal Server Error").is_visible():
            tag = "error500"
            if verbose: print("⚠️ ارور 500 (Server Error)")
    except Exception:
        pass

    if not tag and stage == "after_submit":
        try:
            if (
                page.locator("text=خطا در ارسال اطلاعات").is_visible()
                or page.locator("text=با زبان انگلیسی وارد کنید").is_visible()
                or page.locator("text=نام کاربری نباید شامل فاصله باشد").is_visible()
                or page.locator("text=رمز نباید شامل فاصله باشد").is_visible()
            ):
                tag = "input_validation_error"
                if verbose: print("⚠️ خطای اعتبارسنجی ورودی‌ها")
        except Exception:
            pass

    if tag and verbose:
        print(f"❌ باگ شناسایی شد: {tag}")
    elif verbose:
        print("✅ مشکلی شناسایی نشد.")

    return tag


# ------------------------------
# باز کردن سایت
# ------------------------------
def open_site(p, url: str):
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.wait_for_load_state("domcontentloaded")
    print(f"✅ سایت باز شد: {url}")
    return browser, context, page


# ------------------------------
# لاگین
# ------------------------------
def login(page, username: str, password: str):
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_timeout(2000)

    bug = detect_and_report_bug(page, stage="after_submit")
    if bug:
        raise Exception(f"Login failed with bug: {bug}")

    print(f"✅ ورود موفق: {username}")


# ------------------------------
# تابع کمکی برای کلیک امن روی یک دکمه با متن
# ------------------------------
def safe_click_text(page, text: str, timeout: int = 5000) -> bool:
    """
    دنبال المان با متن می‌گردد و اگر پیدا شد کلیک می‌کند.
    برمی‌گرداند True اگر کلیک انجام شد، False در غیر این صورت.
    """
    try:
        locator = page.locator(f"text={text}")
        if locator.count() == 0:
            return False
        locator.first.click()
        page.wait_for_timeout(1000)
        return True
    except Exception as e:
        print(f"⚠️ خطا در کلیک روی '{text}': {e}")
        return False


# ------------------------------
# تست چند اکانت — کلیک روی هر بخش و در انتها حساب کاربری
# ------------------------------
def test_multiple_accounts(p, creds: List[Tuple[str, str]]):
    SITE_URL = "https://www.eduland.ir/auth/login"

    browser, context, page = open_site(p, SITE_URL)

    for username, password in creds:
        print(f"\n🔁 تست یوزر: {username}")
        try:
            # 1) لاگین
            login(page, username=username, password=password)

            # 2) ترتیب: درس -> تکالیف -> (در آخر) حساب کاربری
            pre_account_buttons = ["درس", "تکالیف"]
            for btn in pre_account_buttons:
                clicked = safe_click_text(page, btn)
                if clicked:
                    print(f"👉 وارد شدیم: {btn}")
                    page.wait_for_timeout(1000)
                    try:
                        page.go_back()
                        page.wait_for_load_state("domcontentloaded")
                    except Exception:
                        pass
                else:
                    print(f"❌ دکمه '{btn}' پیدا یا قابل کلیک نبود.")

            # 3) حساب کاربری
            got_account = safe_click_text(page, "حساب کاربری")
            if got_account:
                print(f"✅ وارد بخش حساب کاربری شدیم: {username}")
            else:
                print(f"❌ نتوانستم وارد حساب کاربری شوم: {username}")

            # 4) خروج
            try:
                logout_btn = page.locator("button:has-text('خروج از حساب')")
                logout_btn.wait_for(state="visible", timeout=5000)
                logout_btn.click()
                print("👉 کلیک روی دکمه خروج")
                try:
                    confirm_btn = page.get_by_text("مطمئنم!")
                    confirm_btn.wait_for(state="visible", timeout=5000)
                    confirm_btn.click()
                    print("🔒 خروج کامل شد")
                except Exception:
                    pass
                page.wait_for_timeout(1000)
            except Exception as e:
                print(f"❌ خطا در خروج: {e}")

            # بازگشت به صفحه لاگین
            page.goto(SITE_URL)
            page.wait_for_load_state("domcontentloaded")

        except Exception as e:
            print(f"❌ خطا برای {username}: {e}")
            try:
                page.goto(SITE_URL)
                page.wait_for_load_state("domcontentloaded")
            except Exception:
                pass

    context.close()
    browser.close()


# ------------------------
# اجرا (خواندن از اکسل)
# ------------------------
if __name__ == "__main__":
    # فایل اکسل باید ستون‌های username و password داشته باشد
    df = pd.read_excel("accounts.xlsx")
    credentials = list(zip(df["username"], df["password"]))

    with sync_playwright() as p:
        test_multiple_accounts(p, credentials)
