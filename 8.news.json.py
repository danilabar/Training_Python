# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json
from pprint import pprint


def top_10_word():
    # открываем файл и добераемся до новостей
    with open('files_8/newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)
        news_item = json_data['rss']['channel']['items']
        dict_desc = dict()
        # получаем каждую новость
        for item in news_item:
            # получаем каждое слово из новости
            item_desc = (item['description']).split(' ')
            for word in item_desc:
                # все слова больше 6 букв пишем в словарь
                if len(word) > 6:
                    key = dict_desc.get(word)
                    if key is None:
                        dict_desc[word] = [0]
                    dict_desc[word][0] += 1

    sorted_word = sorted(dict_desc.items(), key=lambda x: x[1])
    top_word = (sorted_word[-10:])
    print('Топ 10 самых частых слов')
    for top in top_word:
        print(f'Слово "{top[0]}" встречается {top[1][0]} раз')


top_10_word()