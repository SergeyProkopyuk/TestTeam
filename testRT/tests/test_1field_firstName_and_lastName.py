import pytest
from conftest import driver
from settings import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_firstName_lasstName_empty_fields():
    """При регистрации оставить поля 'имя' и 'фамилия' пустыми """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на пустые поля 'имя' и 'фамилия'
    assert pytest.driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_1character():
    """При регистрации использовать 1 символ кириллицы в полях 'имя' и 'фамилия' """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('А')
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('Р')
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данные в полях 'имя' и 'фамилия'
    assert pytest.driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_2characters():
    """При регистрации использовать 2 символа кириллицы в полях 'имя' и 'фамилия' """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('Ав')
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('Ри')
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что регистрация продолжается
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]')

def test_30characters():
    """При регистрации использовать 30 символов кириллицы в полях 'имя' и 'фамилия' """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('тЦвхщшусСпечдцЮвПМоаНыХЦтвнбръ')
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('КкЬУЙПйзгйылщЦоСШютбаНМЩякЫУоК')
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что регистрация продолжается
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]')

def test_31character():
    """При регистрации использовать 31 символ кириллицы в полях 'имя' и 'фамилия' """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('ЪЫЩуяЩКзЫавчХймШГМЪБдмзщМФжоутЪ')
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('ДЫИЙТщЮпуЭГЩЯыЛйЮлблЙагЗЮшВнФУД')
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидныые данные в полях 'имя' и 'фамилия'
    assert pytest.driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')

def test_special_characters():
    """При регистрации использовать спецсимволы в полях 'имя' и 'фамилия' """
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys('В,ас\ил!ий')
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys('Ив}ан[чен+ко')
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данные в полях 'имя' и 'фамилия'
    assert pytest.driver.find_element(By.XPATH, '//span[contains(text(), "Необходимо заполнить поле кириллицей. От 2 до 30 символов.")]')