import pytest
from conftest import driver
from settings import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registered_email():
    """При регистрации указать email который уже привязан к созданной учетной записи"""
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
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password_confirmation)
    #Нажимаем на кнопку 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[@name="register"]').click()

    #Проверяем, что система выдает предупреждение о существующей учетной записи
    assert pytest.driver.find_element(By.XPATH, '//h2[@class="card-modal__title" and contains(text(), "Учётная запись уже существует")]')

def test_authorization_email():
    """Авторизация по почте"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Нажимаем на вкладку "почта"
    pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-mail"]').click()
    #Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)

    #Нажимаем на кнопку 'Войти'
    pytest.driver.find_element(By.XPATH, '//button[@id="kc-login"]').click()

    #Успешный вход в аккаунт
    assert pytest.driver.find_element(By.XPATH, '//h2[@class="user-name user-info__name"]')

def test_authorization_login():
    """Авторизация по логину"""
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@id="kc-register"]')))

    #Нажимаем на вкладку "логин"
    pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-login"]').click()
    #Вводим логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    #Вводим пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)

    #Нажимаем на кнопку 'Войти'
    pytest.driver.find_element(By.XPATH, '//button[@id="kc-login"]').click()

    #Успешный вход в аккаунт
    assert pytest.driver.find_element(By.XPATH, '//h2[@class="user-name user-info__name"]')

