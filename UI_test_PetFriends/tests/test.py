import pytest
from conftest import driver
from settings import valid_email, valid_password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_show_my_pets():
   """Возможность зайти на страницу 'Мои питомцы'"""
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   #Неявное ожидание
   pytest.driver.implicitly_wait(10)
   myDynamicElement = pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]')
   
   # Переходим на страницу пользователя
   pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]').click()
   #Проверяем, что оказались на странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "polip"





def test_all_pets_are_present():
   """Количество питомцев из статистики пользователя
   совпадает с количеством карточек питомцев"""
   #Повторяем действия из теста "test_show_my_pets"(переход на страницу "Мои питомцы")
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]').click()

   #Неявное ожидание
   pytest.driver.implicitly_wait(10)
   myDynamicElement = pytest.driver.find_elements(By.XPATH, '//tbody /tr')

   #Количество карточек питомцев
   pets = pytest.driver.find_elements(By.XPATH, '//tbody /tr')
   pets = len(pets)

   #Число питомцев из статистики пользователя
   numbers = pytest.driver.find_element(By.CLASS_NAME, 'task3').text
   numbers = numbers.split("\n")[1]
   numbers = numbers.split(" ")[-1]
   numbers = int(numbers)

   #Проверяем, что все питомцы присутствуют на странице
   assert numbers == pets


def test_name_age_breed():
   """"Поля 'имя', 'порода' и 'возраст' не пустые"""
   # Повторяем действия из теста "test_show_my_pets"(переход на страницу "Мои питомцы")
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]').click()

   #Явное ожидание
   element1 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//td[1]')))
   element2 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//td[2]')))
   element3 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//td[3]')))

   #Получаем имена, породу и возраст питомцев
   names = pytest.driver.find_elements(By.XPATH, '//td[1]')
   breed = pytest.driver.find_elements(By.XPATH, '//td[2]')
   age = pytest.driver.find_elements(By.XPATH, '//td[3]')

   # Количество карточек питомцев
   pets = pytest.driver.find_elements(By.XPATH, '//tbody /tr')

   #Проверяем, что имя, порода и возраст не пустые поля
   for i in range(len(pets)):
      assert names[i].text != ''
      assert breed[i].text != ''
      assert age[i].text != ''

def test_different_names():
   """Имена питомцев не повторяются"""
   # Повторяем действия из теста "test_show_my_pets"(переход на страницу "Мои питомцы")
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]').click()

   #Явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//td[1]')))

   #Получаем имена питомцев
   name = pytest.driver.find_elements(By.XPATH, '//td[1]')

   #Создаем пустые списки
   all_names =[]
   duplicates =[]

   #Перебираем имена питомцев и заносим их в список "all_names"
   for i in range(len(name)):
      names = name[i].text.replace('\n', '').replace('*', '')
      split_names = names.split(' ')
      all_names.append(split_names)

   #Перебираем значения из списка "all_names" и заносим
   #повторяющиеся значения в список "duplicates"
   for item in all_names:
      if all_names.count(item) > 1 and item not in duplicates:
         duplicates.append(item)
   if duplicates != '':
      print("У питомцев есть повторяющиеся имена.")
   else:
      print("У питомцев нет повторяющихся имен.")

   #Проверяем, что список "duplicates" пустой(нет повторяющихся имен)
   assert duplicates == ''

def test_no_duplicates_pets():
   """Нет одинаковых питомцев"""
   # Повторяем действия из теста "test_show_my_pets"(переход на страницу "Мои питомцы")
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   pytest.driver.find_element(By.XPATH, '//a[@class="nav-link" and contains(text(), "Мои питомцы")]').click()

   #Явное ожидание
   element1 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//tbody /tr[1]')))
   element2 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//tbody /tr[2]')))
   element3 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//tbody /tr[3]')))
   element4 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//tbody /tr[4]')))
   element5 = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//tbody /tr[5]')))

   #Получаем значения питомцев(имя, порода, возраст)
   pets_values1 = pytest.driver.find_elements(By.XPATH, '//tbody /tr[1]')
   pets_values2 = pytest.driver.find_elements(By.XPATH, '//tbody /tr[2]')
   pets_values3 = pytest.driver.find_elements(By.XPATH, '//tbody /tr[3]')
   pets_values4 = pytest.driver.find_elements(By.XPATH, '//tbody /tr[4]')
   pets_values5 = pytest.driver.find_elements(By.XPATH, '//tbody /tr[5]')

   #Создаем пустые списки для хранения значений питомцев
   pet1 = []
   pet2 = []
   pet3 = []
   pet4 = []
   pet5 = []

   #Перебираем значение первого питомца и заносим их в список
   for i in range(len(pets_values1)):
      value1 = pets_values1[i].text.replace('\n', '').replace('*', '')
      split_pet1 = value1.split(' ')
      pet1.append(split_pet1)

   #Преобразуем список первого питомца в множество
   line1 = ''
   for i in pet1:
      line1 += ' '.join(i)
   list_line1 = line1.split(' ')
   set_pet1 = set(list_line1)

   # Перебираем значение второго питомца и заносим их в список
   for i in range(len(pets_values2)):
      value2 = pets_values2[i].text.replace('\n', '').replace('*', '')
      split_pet2 = value2.split(' ')
      pet2.append(split_pet2)

   # Преобразуем список второго питомца в множество
   line2 = ''
   for i in pet2:
      line2 += ' '.join(i)
   list_line2 = line2.split(' ')
   set_pet2 = set(list_line2)

   # Перебираем значение третьего питомца и заносим их в список
   for i in range(len(pets_values3)):
      value3 = pets_values3[i].text.replace('\n', '').replace('*', '')
      split_pet3 = value3.split(' ')
      pet3.append(split_pet3)

   # Преобразуем список третьего питомца в множество
   line3 = ''
   for i in pet3:
      line3 += ' '.join(i)
   list_line3 = line3.split(' ')
   set_pet3 = set(list_line3)

   # Перебираем значение четвертого питомца и заносим их в список
   for i in range(len(pets_values4)):
      value4 = pets_values4[i].text.replace('\n', '').replace('*', '')
      split_pet4 = value4.split(' ')
      pet4.append(split_pet4)

   # Преобразуем список четвертого питомца в множество
   line4 = ''
   for i in pet4:
      line4 += ' '.join(i)
   list_line4 = line4.split(' ')
   set_pet4 = set(list_line4)

   # Перебираем значение пятого питомца и заносим их в список
   for i in range(len(pets_values5)):
      value5 = pets_values5[i].text.replace('\n', '').replace('*', '')
      split_pet5 = value5.split(' ')
      pet5.append(split_pet5)

   # Преобразуем список пятого питомца в множество
   line5 = ''
   for i in pet5:
      line5 += ' '.join(i)
   list_line5 = line5.split(' ')
   set_pet5 = set(list_line5)

   #Проверям, что множества не равны между собой
   assert set_pet1 ^ set_pet2
   assert set_pet1 ^ set_pet3
   assert set_pet1 ^ set_pet4
   assert set_pet2 ^ set_pet3
   assert set_pet2 ^ set_pet4
   assert set_pet2 ^ set_pet5
   assert set_pet3 ^ set_pet4
   assert set_pet3 ^ set_pet5
   assert set_pet4 ^ set_pet5
   assert set_pet1 ^ set_pet5




















