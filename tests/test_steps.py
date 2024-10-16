import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure import attachment_type


@allure.tag("web")
@allure.severity(Severity.TRIVIAL)
@allure.label("QA", "levsavinkov")
@allure.feature("Задачи в репозитории")
@allure.story("Задача в репозитории видна неавторизованному пользователю")
@allure.link("https://github.com", name="Testing")
@allure.id("TEST-1234")
@allure.testcase("https://testit/045hd-123-sds-2321", "Отображение задачи в репозитории")
def test_steps():
    with allure.step("Открываем страницу пользователя"):
        browser.open("/LevSavinkov")
    
    with allure.step("Переходим к списку репозиториев"):
        s(by.xpath("//a[@data-tab-item='repositories']")).click()
    
    with allure.step("Переходим к репозиторию"):
        s(by.xpath("//a[@itemprop='name codeRepository']")).should(have.text("qa.guru_homework_10")).click()
    
    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()
    
    with allure.step("Проверяем наличие Issue с названием My new issue for test"):
        s(by.partial_text("My new issue for test")).should(be.visible)
        html_content = browser.execute_script("return document.documentElement.outerHTML;")
        allure.attach(html_content, name="Html", attachment_type=attachment_type.HTML)
