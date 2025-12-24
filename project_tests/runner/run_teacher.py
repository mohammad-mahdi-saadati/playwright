from core.browser import BrowserManager
from core.reporter import generate_report
import tests_teacher_site.open_site as open_site
import tests_teacher_site.login as login 
import tests_teacher_site.user_account as user_account

tests_list = [open_site, login,user_account]

browser = BrowserManager()
page = browser.start()
results = []

for test_module in tests_list:
    print(f"Running {test_module.__name__} ...")
    result = test_module.run(page)
    results.append(result)

generate_report(results)