from playwright.sync_api import sync_playwright
import random
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Login
        print("\n🔹 Attempting login...")
        page.goto("https://www.eduland.ir/auth/login")
        try:
            page.fill('input[name="username"]', "danesh_t1")
            page.fill('input[name="password"]', "danesh_t1")
            page.click('button[type="submit"]')
            page.wait_for_timeout(2000)
            print("✅ Login successful")
        except Exception as e:
            print(f"❌ Login failed: {str(e)}")
            browser.close()
            return

        # Step 2: Enter exam section
        print("\n🔹 Looking for exam entry button...")
        try:
            page.click("text=کلاس‌ها")
            page.wait_for_timeout(5000)
            print("✅ Exam entry button found and clicked")
        except:
            print("❌ Could not find the exam entry button")
            browser.close()
            return
        try:
            page.click("text=کلاس‌ها")
            page.wait_for_timeout(5000)
            print("✅ Exam entry button found and clicked")
        except:
            print("❌ Could not find the exam entry button")
            browser.close()
            return
        # Step 3: Click the Nth ریاضی button (change only ریاضی_index)
        ریاضی_index = 4  # ← Just change this number (1-based index)

        print(f"\n🔹 Trying to click ریاضی number {ریاضی_index} on the page...")
        try:
            # Select all buttons that have the text ریاضی
            oloum_buttons = page.locator("button:has-text('ریاضی')")

            # Click the Nth ریاضی button (indexing starts from 0 in code)
            oloum_buttons.nth(ریاضی_index - 1).click()

            print(f"✅ Clicked ریاضی number {ریاضی_index} successfully")
        except Exception as e:
            print(f"❌ Failed to click ریاضی number {ریاضی_index}: {str(e)}")


run()