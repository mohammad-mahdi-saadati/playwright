# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
import functions
import re
# ------------------------------
# مقادیر ورودی (قابل تغییر بیرون از تابع)
# ------------------------------
SITE_URL = "https://danio.ir/auth/login"
USERNAME = "danesh.t5"
PASSWORD = "1111"
SUBJECT = "فارسی"
SUBJECT_INDEX = 5
def run():
    with sync_playwright() as p:
        browser, context, page = functions.open_site(p, SITE_URL)
        functions.login(page, USERNAME, PASSWORD)
        functions.click_subject(page, SUBJECT, SUBJECT_INDEX)
        functions.click_skills_by_name(
        page=page,
        skills=functions.farsi5,
        chapters=functions.chapters_farsi5,
        start=20,
        end=40,
        click_subject=(lambda p: functions.click_subject(p, SUBJECT, SUBJECT_INDEX)),
        use_submit_test=False,
        use_go_through_levels=True,
        use_solve_all_level=False
        #subject_index= 3,
        #math_chapter_index=0 
        )

run()
