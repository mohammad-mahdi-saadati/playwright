from core.browser import BrowserManager
from core.reporter import generate_report


tests_list = [open_site, login]

browser = BrowserManager()
page = browser.start()
results = []

for test_module in tests_list:
    print(f"Running {test_module.__name__} ...")
    result = test_module.run(page)
    results.append(result)

generate_report(results)