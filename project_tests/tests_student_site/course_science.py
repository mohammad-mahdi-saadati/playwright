def run(page):
    try:
        page.wait_for_selector("text=علوم", timeout=2000)
        page.click("text=علوم")
        page.wait_for_timeout(800)
        if not page.is_visible("text=علوم"):
            return {
                "name": "enter_math_and_back_test",
                "success": False,
                "error": "Failed to enter Math («علوم)."
            }
        page.go_back()
        page.wait_for_timeout(800)
    except Exception as e:
        return {
            "name": "enter_math_and_back_test",
            "success": False,
            "error": str(e)
        }
