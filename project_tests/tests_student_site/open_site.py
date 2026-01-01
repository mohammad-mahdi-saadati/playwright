def run(page):
    try:
        page.goto("https://www.eduland.ir/auth/login", timeout=5000)
        page.wait_for_timeout(1500)
        print("UA:", page.evaluate("navigator.userAgent"))
        print("WIDTH:", page.evaluate("window.innerWidth"))
        print("HEIGHT:", page.evaluate("window.innerHeight"))
        return {"name": "open_site", "success": True}
    except Exception as e:
        return {"name": "open_site", "success": False, "error": str(e)}
