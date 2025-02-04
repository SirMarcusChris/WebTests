from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    LOGIN_BY_QR_TAB = (By.XPATH, '//*[@data-l="t,get_qr"]')
    LOGIN_FIELD = (By.ID, 'field_email')  # Если есть id, можно написать By.ID и искать по ID
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="external-oauth-login-footer"]/a[@data-l="t,register"]')
    VK_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    MAIL_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    ERROR_TEST = (By.XPATH, '//*[@class="input-e login_error"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_BY_QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAIL_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    def click_login(self):
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def get_login_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEST).text  # Текст возвращается без указания круглых скобок

    def get_password_error_text(self):
        return self.find_element(LoginPageLocators.ERROR_TEST).send_keys('text')
