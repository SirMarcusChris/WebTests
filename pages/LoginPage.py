from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')  #  Если есть id, можно написать By.ID и искать по ID
    LOGIN_BUTTON =(By.XPATH, '//*[@data-l="t,sign_in"]')


class LoginPageHelper(BasePage):
    pass
