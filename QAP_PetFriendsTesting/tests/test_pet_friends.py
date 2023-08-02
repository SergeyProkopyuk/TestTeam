import os.path

from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    """Проверяем возможность получить API ключ при авторизации(материал из модуля)."""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

def test_get_all_pets_with_valid_key(filter = ""):
    """Проверяем что запрос всех питомцев возвращает не пустой список(материал из модуля)."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result["pets"]) > 0

def test_add_new_pet_with_valid_data(name = "котяра", animal_type = "кот", age = 2, pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца(материал из модуля)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result["name"] == name

def test_successful_update_self_pet_info(name="чумазый", animal_type="кошакер", age=5):
    """Проверяем возможность обновления информации о питомце(материал из модуля)."""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets["pets"]) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets["pets"][0]["id"], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result["name"] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца(материал из модуля)."""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets["pets"]) == 0:
        pf.add_new_pet(auth_key, "котяра", "кот", "2", "images/test_cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets["pets"][0]["id"]
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_add_new_pet_without_photo_valid_data(name = "котяра", animal_type = "кот", age = 2):
    """Проверяем возможность добавить нового питомца без фото(практическое задание)."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result["name"] == name

def test_successful_update_pet_photo(pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить фото созданному питомцу(практическое задание)."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets["pets"]) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets["pets"][0]["id"], pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        assert status == 200
        assert result["pet_photo"] != " "
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_with_unvalid_data1(name = "котяра", animal_type = "кот", age = "jgh", pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца, возраст указываем буквами(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_data2(name = " ", animal_type = "кот", age = 2, pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца, оставить поле 'имя' пустым(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_data3(name = "котяра ", animal_type = " ", age = 2, pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца, оставить поле 'тип животного' пустым(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_data4(name = "котяра ", animal_type = "кот", age = " ", pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца, оставить поле 'возраст' пустым(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_data5(name = " ", animal_type = " ", age = " "):
    """Проверяем возможность добавить нового питомца, оставляем все поля пустыми(практическое задание)."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_data6(name = "котяра ", animal_type = "кот", age = 2, pet_photo = "images/test_cat.jpg", pet_photo2 = "images/test_cat2.jpg"):
    """Проверяем возможность добавить нового питомца, добавив 2 фото(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_photo2 = os.path.join(os.path.dirname(__file__), pet_photo2)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet2(auth_key, name, animal_type, age, pet_photo, pet_photo2)
    assert status == 400
    assert result["name"] == name

def test_add_new_pet_with_unvalid_key(name = "мурзик", animal_type = "кот", age = 2, pet_photo = "images/test_cat.jpg"):
    """Проверяем возможность добавить нового питомца, указав не правильный API key(практическое задание)."""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet3(auth_key, name, animal_type, age, pet_photo)
    assert status == 403

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца, указав не правильный API key(практическое задание)."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets["pets"]) == 0:
        pf.add_new_pet(auth_key, "котяра", "кот", "2", "images/test_cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets["pets"][0]["id"]
    status, _ = pf.delete_pet2(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 403
    assert pet_id not in my_pets.values()
