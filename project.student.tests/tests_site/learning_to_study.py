def run(page):
    try:
        icon_selector = "div.MuiBox-root svg"

        if not page.is_visible(icon_selector):
            return {
                "name": "click_icon_and_study",
                "success": False,
                "error": "The required green icon was not found."
            }

        page.click(icon_selector)
        page.wait_for_timeout(600)

        lesson_selector = 'a[href="/student/courses/"]'

        page.wait_for_selector(lesson_selector, timeout=3000)
        page.click(lesson_selector)

        page.wait_for_timeout(800)

        science = page.is_visible("text=علوم")
        math = page.is_visible("text=ریاضی")
        literature = page.is_visible("text=فارسی")

        if not (science and math and literature):
            return {
                "name": "click_icon_and_study",
                "success": False,
                "error": "Lesson tabs not visible ❌"
            }

        return {
            "name": "click_icon_and_study",
            "success": True,
            "message": "✔ Icon click → lesson → tabs OK"
        }

    except Exception as e:
        return {
            "name": "click_icon_and_study",
            "success": False,
            "error": str(e)
        }
