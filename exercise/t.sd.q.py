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
            page.fill('input[name="username"]', "summer_quiz.s51")
            page.fill('input[name="password"]', "1111")
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
            page.click("text=ورود به آزمون تابستانه")
            page.wait_for_timeout(5000)
            print("✅ Exam entry button found and clicked")
        except:
            print("❌ Could not find the exam entry button")
            browser.close()
            return
        # CONFIGURATION - Change this number to select which button to click
        BUTTON_POSITION = 2 # Change this to 1, 2, 3, etc. as needed

        # Step 3: Click the nth exam button found on the page
        print(f"\n🔹 Looking for exam button at position {BUTTON_POSITION}...")

        try:
            # Find all exam buttons (both continue and start)
            all_exam_buttons = page.locator("button:has-text('ادامه آزمون'), button:has-text('شروع آزمون')").all()
            
            if len(all_exam_buttons) < BUTTON_POSITION:
                print(f"❌ Only found {len(all_exam_buttons)} exam buttons (need at least {BUTTON_POSITION})")
                browser.close()
                return
            
            # Select the button at the specified position (adjusting for zero-based index)
            button = all_exam_buttons[BUTTON_POSITION - 1]
            button_text = button.inner_text().strip()
            
            print(f"ℹ️ Found button at position {BUTTON_POSITION}: '{button_text}'")
            
            # Click the button
            button.click()
            print(f"✅ Clicked the button: '{button_text}'")

            # Handle confirmation if it's a "Start Exam" button
            if "شروع آزمون" in button_text:
                page.wait_for_timeout(500)
                try:
                    confirm_button = page.locator("text=مطمئنم").first
                    if confirm_button.is_visible():
                        confirm_button.click()
                        print("✅ Confirmed exam start")
                except:
                    print("⚠️ No confirmation popup appeared")

            page.wait_for_timeout(3000)  # Wait for exam to load

        except Exception as e:
            print(f"❌ Failed to start the exam: {str(e)}")
            browser.close()
            return
        # Step 4: Verify starting question (Fixed)
        print("\n🔹 Verifying starting question...")
        max_attempts = 20
        current_attempt = 0
        question_found = False

        while current_attempt < max_attempts:
            try:
                if page.locator("text= سوال ۲۰ / ۱").is_visible():
                    question_found = True
                    break

                print(f"Attempt {current_attempt + 1}: Clicking '<' to go to first question")

                # More specific selector for navigation buttons
                prev_button = page.locator("button.rtl-1r6flmo").first
                
                if prev_button.is_visible():
                    prev_button.click()
                    page.wait_for_timeout(1000)
                else:
                    print("❌ Previous button is not visible")
                    break

            except Exception as e:
                print(f"❌ Couldn't click previous button: {str(e)}")
                break

            current_attempt += 1

        # ... [rest of your code remains the same until the navigation part]

        # Step 5: Answer questions (Fixed navigation)
        print("\n🔹 Starting to answer questions...")
        for q in range(20):
            page.wait_for_timeout(1000)
            print(f"\n🔸 Question {q + 1}")

            # [Insert your logic to answer the question here...]

            # 🔹 Move to next question (if not last one)
            if q < 19:
                try:
                    # More specific selector for next button
                    next_button = page.locator("button.rtl-1r6flmo").last
                    if next_button.is_visible():
                        next_button.click()
                        print("✅ Clicked NEXT button")
                        page.wait_for_timeout(1500)
                    else:
                        print("❌ NEXT button not visible - using ArrowRight fallback")
                        page.keyboard.press("ArrowRight")
                except Exception as e:
                    print(f"⚠️ Error clicking NEXT button: {str(e)}")
                    try:
                        page.keyboard.press("ArrowRight")
                    except:
                        print("⚠️ Even ArrowRight failed")


run()


