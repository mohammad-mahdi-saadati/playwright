def run(page):
    try:
        page.wait_for_timeout(1000)
        if page.is_visible("text=کلاس",timeout=5000):
            page.click("text=کلاس")
            page.wait_for_timeout(1500)
        else:
            return {"success": False, "error": "Button «کلاس» was not visible.","name": "classes_test"}
        required_buttons = [
            #"پروین اعتصامی",
            #"کلاس پنجم",
            "دبیران",
            "همکلاسی‌ها",
            "مصطفی محمدی",
            "زهرا اصغری",
        ] 
        for w in required_buttons:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found : "{w}"',"name": "classes_test"}
        page.click(".MuiButtonBase-root.rtl-1uifrwd",timeout=5000)
        page.wait_for_timeout(1000)
        required_buttons2 = ["پروین اعتصامی", "عکس", "xacaz"]
        for w in required_buttons2:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found : "{w}"',"name": "classes_test"}
        page.click("text=عکس",timeout=5000)
        page.wait_for_timeout(4000)
        page.locator("button:has(svg)").first.click()

 
        return {"success": True, "name": "classes_test"}

    except Exception as e:
        return {"success": False, "error": str(e), "name": "classes_test"}
