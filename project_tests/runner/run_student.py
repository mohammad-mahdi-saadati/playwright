from project_tests.core.browser import BrowserManager
from project_tests.core.reporter import generate_report

import project_tests.tests_student_site.open_site as open_site
import project_tests.tests_student_site.login as login
import project_tests.tests_student_site.quiz as quiz
import project_tests.tests_student_site.homework as homework
import project_tests.tests_student_site.homework_current_literature as homework_current_literature
import project_tests.tests_student_site.homework_current_science as homework_current_science
import project_tests.tests_student_site.homework_current_math as homework_current_math
import project_tests.tests_student_site.homework_past_literature as homework_past_literature
import project_tests.tests_student_site.homework_past_science as homework_past_science
import project_tests.tests_student_site.homework_past_math as homework_past_math
import project_tests.tests_student_site.homework_future_literature as homework_future_literature
import project_tests.tests_student_site.homework_future_science as homework_future_science
import project_tests.tests_student_site.homework_future_math as homework_future_math
import project_tests.tests_student_site.poshtibany as poshtibany
import project_tests.tests_student_site.learning_to_homeworks as learning_to_homeworks
import project_tests.tests_student_site.learning_to_study as learning_to_study
import project_tests.tests_student_site.performance as performance
import project_tests.tests_student_site.classes as classes
import project_tests.tests_student_site.user_account as user_account
import project_tests.tests_student_site.course_math as course_math
import project_tests.tests_student_site.course_science as course_science
import project_tests.tests_student_site.course_literature as course_literature


tests_list = [open_site, login,
user_account,quiz,performance,classes,homework,
homework_current_literature,homework_current_science,homework_current_math,
homework_past_literature,homework_past_science,homework_past_math,
homework_future_literature,homework_future_science,homework_future_math,
learning_to_study,course_math,course_science,course_literature,
poshtibany]



browser = BrowserManager()
page = browser.start()
results = []

for test_module in tests_list:
    print(f"Running {test_module.__name__} ...")
    result = test_module.run(page)
    results.append(result)

generate_report(results)
