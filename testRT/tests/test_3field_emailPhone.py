import pytest
from conftest import driver
from settings import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_email_phone_empty_field():
    """При регистрации оставить поле 'email или мобильный телефон' пустым"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на пустое поле 'Email или мобильный телефон'
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_invalid_email():
    """При регистрации в поле 'email или мобильный телефон' ввести невалидный email"""
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
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys('kiyom66542@@elixirsd.com')
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в поле 'Email или мобильный телефон'
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')

def test_invalid_phone():
    """При регистрации в поле 'email или мобильный телефон' ввести невалидный номер телефона"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Переходим на форму регистрации
    pytest.driver.find_element(By.XPATH, '//a[@id="kc-register"]').click()
    #Вводим имя в поле "имя"
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(valid_firstName)
    #Вводим фамилию в поле "фамилия"
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(valid_lastName)
    #Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys('+7968276984')
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    #Вводим подтверждение пароля
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает ошибку на невалидные данне в поле 'Email или мобильный телефон'
    assert pytest.driver.find_element(By.XPATH, '//span[@class="rt-input-container__meta rt-input-container__meta--error"]')