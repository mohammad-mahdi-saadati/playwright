import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.eduland.ir/")
    page.get_by_role("link", name="ورود").click()
    page.get_by_role("textbox", name="نام کاربری").click()
    page.get_by_role("textbox", name="نام کاربری").fill("danesh_t1")
    page.get_by_role("textbox", name="رمز عبور").click()
    page.get_by_role("textbox", name="رمز عبور").fill("danesh_t1")
    page.get_by_role("button", name="ورود").click()
    page.get_by_role("button", name="کلاس‌ها").click()
    page.locator("div:nth-child(3) > .MuiPaper-root > div > div > div:nth-child(2) > div:nth-child(2) > button:nth-child(3)").click()
    page.get_by_role("tab", name="مهارت‌ها").click()
    page.get_by_role("link", name="بخش اول ۰%").nth(2).click()
    page.locator("#question-container div").filter(has_text="در زیر بال بیشتر است").nth(4).click()
    page.get_by_role("button", name="ارسال پاسخ").click()
    page.get_by_role("button", name="گرفتم").click()
    page.get_by_role("button", name="ارسال پاسخ").click()
    page.get_by_role("button", name="تایید").click()
    page.get_by_role("button", name="گرفتم").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
