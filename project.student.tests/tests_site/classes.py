def run(page):
    try:
        page.wait_for_timeout(400)
        if page.is_visible("text=کلاس"):
            page.click("text=کلاس")
            page.wait_for_timeout(1200)
        else:
            return {"success": False, "error": "Button «کلاس» was not visible.","name": "classes_test"}
        required_buttons = [
            "پروین اعتصامی",
            "دبیران",
            "مریم میرزاخانی",
            "کلاس پنجم",
        ] 
        for w in required_buttons:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found : "{w}"',"name": "classes_test"}
        page.click(".MuiButtonBase-root.rtl-1uifrwd")
        page.wait_for_timeout(900)
        required_buttons2 = ["پروین اعتصامی", "عکس", "xacaz"]
        for w in required_buttons2:
            if not page.is_visible(f"text={w}"):
                return {"success": False, "error": f'not found : "{w}"',"name": "classes_test"}
        page.click("text=عکس")
        page.wait_for_timeout(1200)
        page.locator("button:has(svg)").first.click()

 
        return {"success": True, "name": "classes_test"}

    except Exception as e:
        return {"success": False, "error": str(e), "name": "classes_test"}
