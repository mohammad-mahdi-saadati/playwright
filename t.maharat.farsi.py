from playwright.sync_api import sync_playwright
import random
import time
def get_skill_list(page):
    """
    گرفتن لیست اسم همه مهارت‌ها (کارت‌ها) در یک درس
    """
    cards = page.locator("div.card-body")
    count = cards.count()
    skill_names = []

    for i in range(count):
        text = cards.nth(i).inner_text().strip()
        # اگه خالی بود یه اسم پیش‌فرض بساز
        if not text:
            text = f"Skill_{i+1}"
        skill_names.append(text)
    print(skill_names)
get_skill_list()
