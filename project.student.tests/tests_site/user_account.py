def run(page):
    try:
        page.wait_for_timeout(400)

        # ورود به پروفایل
        page.wait_for_selector('a[href="/student/profile"] svg', timeout=2000)
        page.click('a[href="/student/profile"] svg')
        page.wait_for_timeout(600)

        required_buttons = [
            "علامه دهخدا",
            "همه نشان‌ها",
            "اطلاعات شخصی",
        ]
        for w in required_buttons:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found: "{w}"', "name": "user_account_test"}

        page.click("text=همه نشان‌ها")
        page.wait_for_timeout(900)

        required_buttons2 = [
            "نشان دقت",
            "نشان سوال",
            "آخرین ‌نشان‌ شما"
        ]
        for w in required_buttons2:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found: "{w}"', "name": "user_account_test"}

        # بازگشت به student
        page.wait_for_selector('a[href="/student"] svg', timeout=2000)
        page.click('a[href="/student"] svg')

        # اطمینان از بازگشت
        page.wait_for_url("**/student", timeout=3000)

        return {"success": True, "name": "user_account_test"}

    except Exception as e:
        return {"success": False, "error": str(e), "name": "user_account_test"}
