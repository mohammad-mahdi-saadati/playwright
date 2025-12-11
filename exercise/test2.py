import pandas as pd
from playwright.sync_api import sync_playwright
import functions

def test_multiple_accounts(p, creds):
    SITE_URL = "https://www.eduland.ir/auth/login"

    browser, context, page = functions.open_site(p, SITE_URL)

    for username, password in creds:
        print(f"\n🔁 تست یوزر: {username}")
        try:
            # 1) لاگین
            functions.login(page, username=username, password=password)

            # 2) چک و کلیک روی دکمه‌ها
            try:
                menu_buttons = ["درس", "تکالیف", "حساب کاربری"]

                found = False
                for btn in menu_buttons:
                    locator = page.locator(f"text={btn}")
                    if locator.count() > 0:
                        locator.first.click()
                        page.wait_for_timeout(1000)
                        print(f"👉 کلیک روی: {btn}")
                        if btn == "حساب کاربری":
                            found = True

                if found:
                    print(f"✅ ورود موفق و باز شدن حساب کاربری: {username}")
                else:
                    print(f"❌ دکمه‌های لازم پیدا نشد: {username}")
                    functions.detect_and_report_bug(
                        page,
                        chapter="system",
                        skill="login_check",
                        stage=f"{username}_no_buttons"
                    )
            except Exception as e:
                print(f"❌ خطا در کلیک روی دکمه‌ها: {e}")
                functions.detect_and_report_bug(
                    page,
                    chapter="system",
                    skill="login_check",
                    stage=f"{username}_click_error"
                )

            # 3) خروج
            try:
                logout_btn = page.locator("button:has-text('خروج از حساب')")
                logout_btn.wait_for(state="visible", timeout=5000)
                logout_btn.click()
                print("👉 کلیک روی دکمه خروج")
                confirm_btn = page.get_by_text("مطمئنم!")
                confirm_btn.wait_for(state="visible", timeout=5000)
                confirm_btn.click()
                print("🔒 خروج کامل شد")

                page.wait_for_timeout(1000)

            except Exception as e:
                print(f"❌ خطا در خروج: {e}")

            # برگشت به صفحه لاگین برای یوزر بعدی
            page.goto(SITE_URL)
            page.wait_for_load_state("domcontentloaded")

        except Exception as e:
            print(f"❌ خطا برای {username}: {e}")

    # آخر کار مرورگر بسته بشه
    context.close()
    browser.close()


# ------------------------
# استفاده
# ------------------------
if __name__ == "__main__":
    
    df = pd.read_excel("accounts.xlsx")

    credentials = list(zip(df["username"], df["password"]))

    with sync_playwright() as p:
        test_multiple_accounts(p, credentials)
