from project_tests.core.browser import BrowserManager
from project_tests.core.reporter import generate_report
import  project_tests.tests_teacher_site.open_site as open_site
import  project_tests.tests_teacher_site.login as login 
import  project_tests.tests_teacher_site.user_account as user_account
import  project_tests.tests_teacher_site.student as student


tests_list = [open_site, login,user_account
              #,student 
               ]

browser = BrowserManager()
page = browser.start()
results = []

for test_module in tests_list:
    print(f"Running {test_module.__name__} ...")
    result = test_module.run(page)
    results.append(result)

generate_report(results)