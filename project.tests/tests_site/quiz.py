def run(page):
    try:
        page.click("text=آزمون", timeout=3000)
        page.wait_for_timeout(800)
        required_tests = [
            ("فارسی", "آبان ماه"),
            ("ریاضی", "آبان ماه"),
            ("علوم", "آبان ماه"),
        ]
        missing_tests = []
        for lesson, month in required_tests:
            lesson_selector = f"text=آزمون {lesson}"
            month_selector = f"text={month}"
            if not page.is_visible(lesson_selector):
                missing_tests.append(f"آزمون {lesson}")
                continue
            if not page.is_visible(month_selector):
                missing_tests.append(f"ماه {month} برای آزمون {lesson}")
                continue
        if missing_tests:
            return {
                "name": "exam_check",
                "success": False,
                "error": f"❌ آزمون‌های زیر پیدا نشدند: {', '.join(missing_tests)}"
            }
        return {
            "name": "exam_check",
            "success": True,
            "message": "✔ تمام آزمون‌های آبان ماه (فارسی، ریاضی، علوم) موجود هستند."
        }
    except Exception as e:
        return {
            "name": "exam_check",
            "success": False,
            "error": str(e)
        }
