from selenium.webdriver.support.wait import WebDriverWait  # Импорт класса WebDriverWeb. Класс, который позволяет
# сказать драйверу, что нужно подождать, когда наступит момент, либо пока не наступит момент
from selenium.webdriver.support import expected_conditions  # Здесь перечислены различные условия

class BasePage:
    def __init__(self, driver):  # Передаём драйвер, который создаётся в фикстуре
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator),
                                                      message=f'Не удалось найти элемент {locator}') # В данном случае
        # find_element получает локатор, найдёт его, подождёт, пока элемент станет видимым. И Return вернёт то,
        # что будет происходить с Веб-элементом. По нему можно кликнуть, вписать текст и ТД.

    def get_url(self, url):
        return self.driver.get(url)
