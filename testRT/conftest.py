import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
   pytest.driver = webdriver.Chrome('D:\Downloads\chromedriver-win64\chromedriver.exe')
   pytest.driver.maximize_window()
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/'
                     'auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/'
                     'login&response_type=code&scope=openid&state=917e835b-864a-4f47-8557-b2df8bd29e6e&theme&auth_type')

   yield

   pytest.driver.quit()