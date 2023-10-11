import pytest
from conftest import driver
from settings import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_password_password_confirmation_empty_field():
    """При регистрации оставить поля 'Пароль' и 'Подтверждение пароля' пустыми"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на пустые поля "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_7characters():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" 7 символов"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('woMj3NW')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('woMj3NW')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_8characters():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" 8 символов"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('W8I7HxRf')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('W8I7HxRf')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что регистрация продолжается
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]')

def test_20characters():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" 20 символов"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Ai8UIfIEYnaklHIKYEzi')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('Ai8UIfIEYnaklHIKYEzi')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что регистрация продолжается
    assert pytest.driver.find_element(By.XPATH, '//h1[@class="card-container__title"]')

def test_21characters():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" 21 символ"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('y0XqtQPDeOwMOLmUdQedf')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('y0XqtQPDeOwMOLmUdQedf')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_Cyrillic():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" пароль кириллицей"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Пткпвщпк')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('Пткпвщпк')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_no_capital_letter():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" пароль без заглавной буквы"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('wehtj7gf')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('wehtj7gf')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_without_numbers_and_special_characters():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" пароль без цифр и спецсимволов"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Qwertyui')
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('Qwertyui')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_carved_passwords():
    """При регистрации ввести в поля "Пароль" и "Подтверждение пароля" разные пароли"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys('Qwer1239')
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в полях "Пароль" и "Подтверждение пароля"
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')