TAB = "آینده"
LESSON = "فارسی"
TASK_NUMBER = "چهارم"   
def run(page):
    try:
        page.click(f"text={TAB}", timeout=4000)
        page.wait_for_timeout(500)

        if not page.is_visible(f"text={LESSON}"):
            return {
                "name": f"task_test_{TAB}_{LESSON}",
                "success": False,
                "error": f"❌ Lesson '{LESSON}' was not found in tab '{TAB}'."
            }

        page.click(f"text={LESSON}", timeout=4000)
        page.wait_for_timeout(800)

        task_found = (
            page.is_visible(f"text=تکلیف‌ {TASK_NUMBER}") or
            page.is_visible(f"text=تکلیف {TASK_NUMBER}")
        )

        if not task_found:
            return {
                "name": f"task_test_{TAB}_{LESSON}",
                "success": False,
                "error": f"❌ Task {TASK_NUMBER} was not found in tab '{TAB}' and lesson '{LESSON}'."
            }

        return {
            "name": f"task_test_{TAB}_{LESSON}",
            "success": True,
            "message": f"✔ Task {TASK_NUMBER} was found in lesson '{LESSON}' and tab '{TAB}'."
        }

    except Exception as e:
        return {
            "name": f"task_test_{TAB}_{LESSON}",
            "success": False,
            "error": f"Exception: {str(e)}"
        }
