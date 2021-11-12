# У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон
# https://yandex.ru/dev/disk/poligon/. Нужно написать программу, которая принимает на вход путь до файла на компьютере и
# сохраняет на Яндекс.Диск с таким же именем.
#
# Все ответы приходят в формате json;
# Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
# Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
# HOST: https://cloud-api.yandex.net:443
#
# Шаблон для программы
#
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загруджает файл file_path на яндекс диск"""
#         # Тут ваша логика
#         return 'Вернуть ответ об успешной загрузке'
#
#
# if __name__ == '__main__':
#     uploader = YaUploader('<Your Yandex Disk token>')
#     result = uploader.upload('c:\my_folder\file.txt')

import os

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        self.file_path = file_path
        # Получить ссылку на загрузку файлов на яндекс диск
        file_name = os.path.basename(self.file_path)
        resp = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": "/" + file_name, "overwrite": "true"},
            headers={"Authorization": "OAuth " + self.token}
        )

        resp.raise_for_status()
        d = resp.json()
        # pprint(d) # получили ссылку href и метод PUT
        href = d["href"]

        # Отправляем файл

        with open(self.file_path, "rb") as f:
            resp2 = requests.put(href, files={"file": f})

        resp2.raise_for_status()

        return print('Файл успешно загружен')


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload('C:\Temp\TEST_Upload.txt')