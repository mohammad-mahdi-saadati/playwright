TAB = "گذشته"     
LESSON = "ریاضی"   
def run(page):
    try:
        page.click(f"text={TAB}", timeout=2000)
        page.wait_for_timeout(500)
        if not page.is_visible(f"text={LESSON}"):
            return {
                "name": f"task_test_{TAB}_{LESSON}",
                "success": False,
                "error": f"❌ درس «{LESSON}» در تب «{TAB}» پیدا نشد."
            }
        page.click(f"text={LESSON}", timeout=2000)
        page.wait_for_timeout(800)
        task_found = page.is_visible("text=تکلیف‌ چهارم") or page.is_visible("text=تکلیف چهارم")
        if not task_found:
            return {
                "name": f"task_test_{TAB}_{LESSON}",
                "success": False,
                "error": f"❌ در تب «{TAB}» و درس «{LESSON}» تکلیف چهارم یافت نشد!"
            }
        return {
            "name": f"task_test_{TAB}_{LESSON}",
            "success": True,
            "message": f"✔ تکلیف چهارم در درس «{LESSON}» و تب «{TAB}» پیدا شد."
        }
    except Exception as e:
        return {
            "name": f"task_test_{TAB}_{LESSON}",
            "success": False,
            "error": f"Exception: {str(e)}"
        }
