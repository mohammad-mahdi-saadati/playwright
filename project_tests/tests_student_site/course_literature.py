def run(page):
    try:
        page.wait_for_selector("text=فارسی", timeout=4000)
        page.click("text=فارسی")
        page.wait_for_timeout(800)
        if not page.is_visible("text=فارسی"):
            return {
                "name": "enter_math_and_back_test",
                "success": False,
                "error": "Failed to enter Math («فارسی»)."
            }
        page.go_back()
        page.wait_for_timeout(800)
    except Exception as e:
        return {
            "name": "enter_math_and_back_test",
            "success": False,
            "error": str(e)
        }
