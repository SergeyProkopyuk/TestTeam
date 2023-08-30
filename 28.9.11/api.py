import pytest
import requests


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):
        """Авторизация пользователя и получение API ключа."""

        headers = {
            "email" : email,
            "password" : password,
        }
        res = requests.get(self.base_url + "api/key", headers = headers)
        status = res.status_code
        result = ""

        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """Список питомцев согласно фильтру."""
        headers = {"auth_key" : auth_key["key"]}
        filter = {"filter" : filter}

        res = requests.get(self.base_url + "api/pets", headers = headers, params = filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        """Добавление нового питомца."""
        data = {
            "name" : name,
            "animal_type" : animal_type,
            "age" : age,
        }
        headers = {"auth_key" : auth_key["key"]}
        file = {"pet_photo" : (pet_photo, open(pet_photo, "rb"), "image/jpg")}
        res = requests.post(self.base_url + "api/pets", headers = headers, data = data, files = file)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet(self, auth_key, pet_id):
        """Удаление питомца."""

        headers = {"auth_key": auth_key["key"]}

        res = requests.delete(self.base_url + "api/pets/" + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def update_pet_info(self, auth_key, pet_id, name,
                        animal_type, age):
        """Обновление данных о питомце."""

        headers = {"auth_key": auth_key["key"]}
        data = {
            "name": name,
            "age": age,
            "animal_type": animal_type
        }

        res = requests.put(self.base_url + "api/pets/" + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_new_pet_without_photo(self, auth_key, name, animal_type, age):
        """Добавление нового питомца без фото."""
        data = {
            "name" : name,
            "animal_type" : animal_type,
            "age" : age,
        }
        headers = {"auth_key" : auth_key["key"]}
        res = requests.post(self.base_url + "/api/create_pet_simple", headers = headers, data = data)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_pet_photo(self, auth_key, pet_id, pet_photo):
        """Добавление фото питомца."""

        headers = {"auth_key": auth_key["key"]}
        file = {"pet_photo": (pet_photo, open(pet_photo, "rb"), "image/jpg")}

        res = requests.post(self.base_url + "/api/pets/set_photo/" + pet_id, headers=headers, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result