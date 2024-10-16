from selene import have
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_with_selene():
    browser.open("/LevSavinkov")
    s(by.xpath("//a[@data-tab-item='repositories']")).click()
    s(by.xpath("//a[@itemprop='name codeRepository']")).should(have.text("qa.guru_homework_10")).click()
    s("#issues-tab").click()
    s(by.partial_text("My new issue for test")).should(be.visible)
