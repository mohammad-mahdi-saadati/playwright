# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import functions
import re
# ------------------------------
# مقادیر ورودی (قابل تغییر بیرون از تابع)
# ------------------------------
SITE_URL = "https://www.eduland.ir/auth/login"
USERNAME = "danesh_t1"
PASSWORD = "danesh_t1"
SUBJECT = "فارسی"
SUBJECT_INDEX = 3
def run():
    with sync_playwright() as p:
        browser, context, page = functions.open_site(p, SITE_URL)
        functions.login(page, USERNAME, PASSWORD)
        functions.click_subject(page, SUBJECT, SUBJECT_INDEX)
        functions.click_skills_by_name(
        page=page,
        skills=functions.farsi3,
        chapters=functions.chapters_farsi3,
        start=0,
        #end=20,
        click_subject=(lambda p: functions.click_subject(p, SUBJECT, SUBJECT_INDEX)),
        use_submit_test=False,
        use_go_through_levels=True
        )

run()
