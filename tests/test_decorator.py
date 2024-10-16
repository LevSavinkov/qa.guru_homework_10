import allure
from allure_commons.types import Severity
from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step("Открываем страницу пользователя")
def open_browser():
    browser.open("/LevSavinkov")


@allure.step("Переходим к списку репозиториев")
def go_to_repo_list():
    s(by.xpath("//a[@data-tab-item='repositories']")).click()


@allure.step("Переходим к репозиторию")
def go_to_repo():
    s(by.xpath("//a[@itemprop='name codeRepository']")).should(have.text("qa.guru_homework_10")).click()


@allure.step("Открываем таб Issues")
def go_to_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием My new issue for test")
def should_issue():
    s(by.partial_text("My new issue for test")).should(be.visible)


def test_with_selene():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label("QA", "levsavinkov")
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Задача в репозитории видна неавторизованному пользователю")
    allure.dynamic.link("https://github.com", name="Testing")
    open_browser()
    go_to_repo_list()
    go_to_repo()
    go_to_issue_tab()
    should_issue()
