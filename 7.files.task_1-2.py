# https://github.com/netology-code/py-homeworks-basic/tree/master/7.files
# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...
# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
# Задача №1
# Должен получится следующий словарь
#
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем
# готовить
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться

def read_file():
    cook_book = {}
    with open('files/recipes.txt', encoding='utf-8') as cook_book_in_file:
        line = cook_book_in_file.readline().strip()
        while line != '':
            dish = line
            count_ingredients = int(cook_book_in_file.readline().strip())
            ingredients = []
            for _ in range(count_ingredients):
                ingredient_line = cook_book_in_file.readline().strip()
                ingredient_info = ingredient_line.split(' | ')
                name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredient_info = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient_info)
            cook_book[dish] = ingredients
            cook_book_in_file.readline()
            line = cook_book_in_file.readline().strip()
    return cook_book
