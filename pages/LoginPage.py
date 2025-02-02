from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BY_QR_TAB = (By.XPATH, '//*[data-l="t,get_qr"]')
    LOGIN_TAB = (By.XPATH, '//*[data-l="t,login_tab"]')
    LOGIN_FIELD = (By.XPATH, '//*[@id="field_email"]')  # Если есть id, можно написать By.ID и искать по ID
    PASSWORD_FIELD = (By.XPATH, '//*[@id="field_password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    LOGIN_BY_QR_BUTTON = (By.XPATH, '//*[@id="qrCode-4532853097"]')
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//*[data-l="t,restore"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@data-l="t,restore""]')


class LoginPageHelper(BasePage):
    pass
