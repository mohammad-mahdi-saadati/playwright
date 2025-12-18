def run(page):
    try:
        page.click('a[href="/student/profile"]')
        page.wait_for_timeout(600)
        for w in ["علامه دهخدا", "همه نشان‌ها", "اطلاعات شخصی"]:
            if not page.is_visible(f"text={w}"):
                return {
                    "success": False,
                    "name": "user_account_test",
                    "error": f'not found: "{w}"'
                }
        page.click("text=همه نشان‌ها")
        page.wait_for_timeout(800)
        for w in ["نشان دقت", "نشان سوال"," نشان‌های شما"]:
            if not page.is_visible(f"text={w}"):
                return {
                    "success": False,
                    "name": "user_account_test",
                    "error": f'not found: "{w}"'
                }
        page.go_back()
        page.wait_for_timeout(600)
        page.go_back()
        page.wait_for_url("**/student", timeout=3000)
        return {
            "success": True,
            "name": "user_account_test"
        }
    except Exception as e:
        return {
            "success": False,
            "name": "user_account_test",
            "error": str(e)
        }
