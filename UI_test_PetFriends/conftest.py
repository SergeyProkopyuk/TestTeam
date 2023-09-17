import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
   pytest.driver = webdriver.Chrome('D:\Downloads\chromedriver-win64\chromedriver.exe')
   pytest.driver.maximize_window()
   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

