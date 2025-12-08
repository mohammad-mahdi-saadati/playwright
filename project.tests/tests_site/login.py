from playwright.sync_api import sync_playwright as p

def login(page, username: str = "danesh_t1", password: str = "danesh_t1"):
    try:
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_timeout(2000)

        print(f"✅ Logged in as {username}")

    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        raise