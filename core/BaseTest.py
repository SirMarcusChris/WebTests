import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()  # Создаём инстанс браузера. В этот момент запускается браузер
    yield driver  # Дальше драйвер работает, ставим на паузу и не продолжаем код. В момент, когда сессия завершится,
    #  браузер закроется
    driver.quit()
