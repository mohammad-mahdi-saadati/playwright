def run(page):
    try:
        page.click("حساب کاربری")
        page.wait_for_timeout(600)
        for w in ["خروج از حساب کاربری", "تغییر رمز", "نام کاربری"]:
            if not page.is_visible(f"text={w}"):
                return {
                    "success": False,
                    "name": "user_account_test",
                    "error": f'not found: "{w}"'
                }
        page.go_back()
        page.wait_for_timeout(600)
    except Exception as e:
        return {
            "success": False,
            "name": "user_account_test",
            "error": str(e)
        }
