def run(page):
    try:
        page.click("text=ورود", timeout=5000)
        page.wait_for_selector('input[name="username"]', timeout=5000)
        page.fill('input[name="username"]', "demo.t1")
        page.fill('input[name="password"]', "1111")
        page.click('button[type="submit"]')
        page.wait_for_timeout(2000)
        required_buttons = [ "پروین", "کلاس های من", "تکالیف جاری", "گزارش تکلیف "]
        all_visible = True
        for btn_text in required_buttons:
            if not page.is_visible(f"text={btn_text}"):
                all_visible = False
                missing_btn = btn_text
                break
        if all_visible:
            return {"name": "login_buttons_check", "success": True}
        else:
            return {
                "name": "login_buttons_check",
                "success": False,
                "error": f"Button '{missing_btn}' was not visible after entering the page"

            }

    except Exception as e:
        return {"name": "login_buttons_check", "success": False, "error": str(e)}
