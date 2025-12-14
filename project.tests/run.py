from core.browser import BrowserManager
from core.reporter import generate_report
import tests_student_site.open_site as open_site
import tests_student_site.login as login 
import tests_student_site.quiz as quiz
import tests_student_site.homework as homework
import tests_student_site.homework_current_literature as homework_current_literature
import tests_student_site.homework_current_science as homework_current_science
import tests_student_site.homework_current_math as homework_current_math
import tests_student_site.homework_past_literature as homework_past_literature
import tests_student_site.homework_past_science as homework_past_science
import tests_student_site.homework_past_math as homework_past_math
import tests_student_site.homework_future_literature as homework_future_literature
import tests_student_site.homework_future_science as homework_future_science
import tests_student_site.homework_future_math as homework_future_math
import tests_student_site.poshtibany as poshtibany
import tests_student_site.learning_to_homeworks as learning_to_homeworks
import tests_student_site.learning_to_study as learning_to_study
import tests_student_site.performance as performance
import tests_student_site.classes as classes
import tests_student_site.user_account as user_account
tests_list = [open_site, login,quiz,performance,classes,homework,
homework_current_literature,homework_current_science,homework_current_math,
homework_past_literature,homework_past_science,homework_past_math,
homework_future_literature,homework_future_science,homework_future_math,
learning_to_study,
poshtibany]



browser = BrowserManager()
page = browser.start()
results = []

for test_module in tests_list:
    print(f"Running {test_module.__name__} ...")
    result = test_module.run(page)
    results.append(result)

generate_report(results)
