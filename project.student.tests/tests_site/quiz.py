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
                "name": "quiz_check",
                "success": False,
                "error": f"❌ The following tests were not found: {', '.join(missing_tests)}"
            }
        return {
            "name": "quiz_check",
            "success": True,
            "message": "✔ All November tests («فارسی», «ریاضی», «علوم») are present."
        }
    except Exception as e:
        return {
            "name": "quiz_check",
            "success": False,
            "error": str(e)
        }
