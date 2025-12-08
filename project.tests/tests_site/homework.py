def run(page):
    try:
        page.wait_for_load_state("domcontentloaded", timeout=2000)
        page.click("text=تکلیف ", timeout=2000)
        page.click("text=همه تکالیف ", timeout=2000)
        page.wait_for_timeout(1000)
        current_visible = page.is_visible("text=جاری")
        future_visible = page.is_visible("text=آینده")
        past_visible = page.is_visible("text=گذشته")
        if future_visible and past_visible and current_visible:
            return {"name": "learning_button_test", "success": True}
        else:
            return {
                "name": "learning_button_test",
                "success": False,
                "error": "درس یا تکلیف ظاهر نشد"
            }
    except Exception as e:
        return {"name": "learning_button_test", "success": False, "error": str(e)}
