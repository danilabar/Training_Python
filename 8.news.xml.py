# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import xml.etree.ElementTree as ET
from pprint import pprint


def top_10_word():
    dict_desc = dict()
    # открываем файл и добераемся до новостей
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("files_8/newsafr.xml", parser)
    root = tree.getroot()
    news_xml = root.findall("channel/item")
    for news in news_xml:
        descr = news.find("description")
        # получаем каждое слово из новости
        item_desc = descr.text.split(' ')
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