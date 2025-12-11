def run(page):
    try:
        page.click("text=پشتیبانی", timeout=3000)
        page.wait_for_timeout(800)
        message_input_selector = 'input[placeholder="پیام خود را بنویسید..."]'
        if not page.is_visible(message_input_selector):
            return {
                "name": "support_test",
                "success": False,
                "error": "❌ The support message input was not found!"
            }
        test_message = "تست"
        page.fill(message_input_selector, test_message)
        page.wait_for_timeout(500)
        send_button_selector = "button._sendBtn_1qqj4_26"
        is_disabled = page.get_attribute(send_button_selector, "disabled")
        if is_disabled is not None:
            return {
                "name": "support_test",
                "success": False,
                "error": "❌ The send button is still disabled! Message was not submitted."
            }
        page.click(send_button_selector, timeout=2000)
        page.wait_for_timeout(1200)
        if not page.is_visible(f"text={test_message}"):
            return {
                "name": "support_test",
                "success": False,
                "error": "❌ Message was sent but did not appear in the message list!"
            }
        return {
            "name": "support_test",
            "success": True,
            "message": "✔ Message was successfully sent and displayed in the chat."
        }
    except Exception as e:
        return {
            "name": "support_test",
            "success": False,
            "error": f"Exception: {str(e)}"
        }
