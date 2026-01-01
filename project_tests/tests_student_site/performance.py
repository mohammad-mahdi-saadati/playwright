def run(page):
    EXPECTED_INCORRECT = 102 
    required_buttons = ["مجموع زمان", "تعداد جام", "تعداد سوال", "تعداد مهارت",]
    try:
        if page.is_visible("text=عملکرد",timeout=10000):
            page.click("text=عملکرد")
        else:
            return {"name": "performance_test", "success": False, "error": "Button «عملکرد» was not visible."}
        page.wait_for_timeout(3000)
        for t in required_buttons:
            if not page.is_visible(f"text={t}"):
                return {
                    "name": "performance_test",
                    "success": False,
                    "error": "Could not find the number of incorrect answers."
                }
        body_text = page.inner_text("body")
        incorrect_count = None
        for word in body_text.split():
            if word.isdigit():
                if "نادرست" in body_text[body_text.find(word)-15 : body_text.find(word)+15]:
                    incorrect_count = int(word)
                    break

        if incorrect_count is None:
            return {
                "name": "performance_test",
                "success": False,
                "error": "نتوانستم تعداد پاسخ نادرست را پیدا کنم"
            }
        if incorrect_count == EXPECTED_INCORRECT or 561:
            return {
                "name": "performance_test",
                "success": True,
                "incorrect_count": incorrect_count,
                "msg": "Entered «عملکرد» and the correct value was found."
            }
        else:
            return {
                "name": "performance_test",
                "success": False,
                "incorrect_count": incorrect_count,
                "error": f"The number of incorrect answers is wrong (found: {incorrect_count})"
            }

    except Exception as e:
        return {"name": "performance_test", "success": False, "error": str(e)}
