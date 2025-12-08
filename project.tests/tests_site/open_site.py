def run(page):
    try:
        page.goto("https://danio.ir/", timeout=5000)
        page.wait_for_timeout(1500)

        return {"name": "open_site", "success": True}

    except Exception as e:
        return {"name": "open_site", "success": False, "error": str(e)}
