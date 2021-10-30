# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort или sorted.

import json
import collections
from pprint import pprint
import xml.etree.ElementTree as ET


def read_json(file_path, len_word=6, top_words=10):
   with open(file_path, 'r', encoding='utf-8') as news_file:
       news = json.load(news_file)
       description_words = []
       for item in news['rss']['channel']['items']:
           description = [word for word in item['description'].split(' ') if len(word) > len_word]
           description_words.extend(description)
       counter_words = collections.Counter(description_words)
       pprint(counter_words.most_common(top_words))


def read_xml(file, len_word=6, top_words=10):
   tree = ET.parse(file)
   root = tree.getroot()
   xml_items = root.findall('channel/item')
   description_words = []
   descriptions = [item.find('description').text.split() for item in xml_items]
   for description in descriptions:
       description = [word for word in description if len(word) > len_word]
       description_words.extend(description)
   counter_words = collections.Counter(description_words)
   pprint(counter_words.most_common(top_words))


if __name__ == '__main__':
   read_json('files_8/newsafr.json')
   print('------')
   read_xml('files_8/newsafr.xml')