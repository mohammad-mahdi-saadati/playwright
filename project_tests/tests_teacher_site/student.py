def run(page):
    try:
        page.click("text=دانش‌آموزان")
        page.wait_for_timeout(800)
        required_texts = [
            "علامه دهخدا",
            "حساب کاربری",
            "نمره میانگین",
            "تکالیف انجام شده",
        ]
        for text in required_texts:
            if not page.is_visible(f"text={text}"):
                return {
                    "success": False,
                    "name": "students_page_basic_check",
                    "error": f'not found: "{text}"'
                }

        search_input = page.locator('input[placeholder="جستجو"]')
        search_input.fill("سینا")
        page.wait_for_timeout(800)

        if not page.is_visible("text=ابوعلی سینا"):
            return {
                "success": False,
                "name": "students_search_test",
                "error": "search result not found"
            }
        search_input.fill("")
        page.wait_for_timeout(500)
        page.click("text=پایه")
        page.wait_for_timeout(300)
        page.click("text=چهارم")
        page.wait_for_timeout(800)
        if page.locator("text=ابو نصر فارابی").count() == 0:
            return {
                "success": False,
                "name": "students_filter_test",
                "error": "no result after filtering by پایه چهارم"
            }

        return {
            "success": True,
            "name": "students_full_test"
        }
    except Exception as e:
        return {
            "success": False,
            "name": "students_full_test",
            "error": str(e)
        }
