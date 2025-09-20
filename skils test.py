# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import def
import re
# ------------------------------
# مقادیر ورودی (قابل تغییر بیرون از تابع)
# ------------------------------
SITE_URL = "https://www.eduland.ir/auth/login"
USERNAME = "saadati.t"
PASSWORD = "1111"
SUBJECT = "علوم"
SUBJECT_INDEX = 3
def run():
    with sync_playwright() as p:
        browser, context, page = t.open_site(p, SITE_URL)
        def.login(page, USERNAME, PASSWORD)
        t.click_subject(page, SUBJECT, SUBJECT_INDEX)
        t.click_skills_by_name(
        page=page,
        skills=t.since3,
        chapters=t.chapters_since3,
        start=3,
        #end=20,
        click_subject=(lambda p: t.click_subject(p, SUBJECT, SUBJECT_INDEX)),
        use_submit_test=True,
        use_go_through_levels=False
        )

run()
