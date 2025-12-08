def run(page):
    try:

        icon_selector = "div.MuiBox-root svg"

        if not page.is_visible(icon_selector):
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "آیکون سبز مورد نظر پیدا نشد"
            }
        page.click(icon_selector, timeout=2000)
        page.wait_for_timeout(600)

        if not page.is_visible("text=درس"):
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "بعد از کلیک روی آیکون، دکمه «درس» پیدا نشد"
            }
        page.click("text=درس", timeout=2000)
        page.wait_for_timeout(800)
        current = page.is_visible("text=جاری")
        future  = page.is_visible("text=آینده")
        past    = page.is_visible("text=گذشته")
        if current and future and past:
            return {
                "name": "click_icon_and_homework",
                "success": True,
                "message": "✔ کلیک روی آیکون و ورود به درس موفقیت‌آمیز بود"
            }
        else:
            return {
                "name": "click_icon_and_homework",
                "success": False,
                "error": "تب‌های درس قابل مشاهده نیستند، ورود ناموفق ❌"
            }
    except Exception as e:
        return {
            "name": "click_icon_and_homework",
            "success": False,
            "error": str(e)
        }
