from core.BaseTest import browser
from  pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://ok.ru/'
EMPTY_LOGIN_ERROR = 'Введите логин'
EMPTY_PASSWORD_ERROR = 'Введите пароль'

def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)

    LoginPage.click_login()
    assert LoginPage.get_login_error_text() == EMPTY_LOGIN_ERROR

def test_empty_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)

    LoginPage.enter_text_in_login_field()
    LoginPage.click_login()
    assert LoginPage.get_password_error_text() == EMPTY_PASSWORD_ERROR
