def run(page):
    try:
        icon_selector = "div.MuiBox-root svg"

        if not page.is_visible(icon_selector):
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "The required green icon was not found."
            }
        page.click(icon_selector, timeout=4000)
        page.wait_for_timeout(600)

        if not page.is_visible("text=تکلیف"):
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "After clicking the icon, the «تکلیف» button was not found ❌"
            }
        page.click("text=تکلیف", timeout=4000)
        page.wait_for_timeout(800)
        current = page.is_visible("text=جاری")
        future  = page.is_visible("text=آینده")
        past    = page.is_visible("text=گذشته")
        if not (current and future and past):
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "The «تکلیف» tabs are not visible; homework entry failed."
            }
        page.wait_for_selector(icon_selector, timeout=4000)
        page.click(icon_selector)
        page.wait_for_timeout(600)

        return {
            "name": "click_icon_and_homework",
            "success": True,
            "message": "✔ Clicking the icon, entering «تکلیف», and returning back was successful."
        }

    except Exception as e:
        return {
            "name": "click_icon_and_homework",
            "success": False,
            "error": str(e)
        }
