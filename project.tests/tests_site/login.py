from playwright.sync_api import sync_playwright as p

def login(page, username: str = "demo.t1", password: str = "demo.t1"):
    try:
        page.click("text=ورود")
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_timeout(2000)

        print(f"✅ Logged in as {username}")

    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        raise
def run(page):
    page.fill('input[name="username"]', "user")
    page.fill('input[name="password"]', "pass")
    page.click('button[type="submit"]')
    page.wait_for_timeout(1500)
    return {"name": "login", "status": "passed"}
