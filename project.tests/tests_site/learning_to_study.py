def run(page):
    try:

        icon_selector = "div.MuiBox-root svg"

        if not page.is_visible(icon_selector):
            return {
                "name": "click_icon_and_study",
                "success": False,
                "error": "The required green icon was not found."
            }
        page.click(icon_selector, timeout=2000)
        page.wait_for_timeout(600)

        if not page.is_visible("text=درس"):
            return {
                "name": "click_icon_and_study",
                "success": False,
                "error": "After clicking the icon, the «درس» button was not found."
            }
        page.click("text=درس", timeout=2000)
        page.wait_for_timeout(800)
        science = page.is_visible("text=علوم")
        math  = page.is_visible("text=ریاضی")
        litereature    = page.is_visible("text=فارسی")
        if science and math and litereature:
            return {
                "name": "click_icon_and_study",
                "success": True,
                "message": "✔ Clicking the icon and entering «درس» was successful."
            }
        else:
            return {
                "name": "click_icon_and_study",
                "success": False,
               "error": "The «درس» tabs are not visible; entry failed ❌"
            }
    except Exception as e:
        return {
            "name": "click_icon_and_study",
            "success": False,
            "error": str(e)
        }
