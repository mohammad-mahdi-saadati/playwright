import re

def run(page):
    try:
        page.click("text=پشتیبانی", timeout=3000)
        page.wait_for_timeout(1000)

        messages = page.locator("text=/تست\\s*\\d+/").all_inner_texts()

        max_number = 0
        for msg in messages:
            match = re.search(r"تست\s*(\d+)", msg)
            if match:
                num = int(match.group(1))
                if num > max_number:
                    max_number = num

        test_message = f"تست {max_number + 1}"

        input_selector = 'input[placeholder="پیام خود را بنویسید..."]'
        page.fill(input_selector, test_message)
        page.wait_for_timeout(500)

        send_button = "button._sendBtn_1qqj4_26"
        page.click(send_button, timeout=2000)
        page.wait_for_timeout(1200)

        if not page.is_visible(f"text={test_message}"):
            return {
                "name": "support_test",
                "success": False,
                "error": "❌ Message not found after sending"
            }

        # 👇 بستن پشتیبانی
        close_button = "div._closeModal_1qqj4_139"
        page.click(close_button, timeout=2000)
        page.wait_for_timeout(500)

        return {
            "name": "support_test",
            "success": True,
            "message": f"✔ Message '{test_message}' sent and support closed successfully"
        }

    except Exception as e:
        return {
            "name": "support_test",
            "success": False,
            "error": str(e)
        }
