# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
#
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
#
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.weight += 1
        print('Животное покормлено')

class Birds(Animals):
    def __init__(self, name, weight, type_bird, voice):
        super().__init__(name, weight)
        self.type_bird = type_bird
        self.voice = voice

    def collect_eggs(self, eggs=2):
        self.eggs = eggs
        self.weight -= (self.eggs * 0.2)
        print(f'Получили яиц {self.eggs}')


class Cows(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Му-у-у'

    def collect_milk(self, liters_milk=1):
        self.liters_milk = liters_milk
        self.weight -= self.liters_milk
        print(f'Получили литров молока {self.liters_milk}')


class Goats(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Бе-е-е'

    def collect_milk(self, liters_milk=1):
        self.liters_milk = liters_milk
        self.weight -= self.liters_milk
        print(f'Получили литров молока {self.liters_milk}')


class Sheep(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Бе-е-е'

    def collect_wool(self, collect_wool=0.8):
        self.collect_wool = collect_wool
        self.weight -= (self.collect_wool * 0.8)
        print(f'Получили кг шерсти {self.collect_wool}')


geese_gray = Birds('Серый', 10, 'Гусь', 'Га-Га-Га')
geese_white = Birds('Белый', 12, 'Гусь', 'Га-Га-Га')
cows_manya = Cows('Манька', 150)
sheep_barashek = Sheep('Барашек', 50)
sheep_kudryaviy = Sheep('Кудрявый', 60)
chicken_koko = Birds('Ко-Ко', 9, 'Курица', 'Ко-ко-ко')
chicken_kukareku = Birds('Кукареку', 8, 'Курица', 'Ко-ко-ко')
goats_roga = Goats('Рога', 45)
goats_kopyta = Goats('Копыта', 47)
chicken_kryakva = Birds('Кряква', 11, 'Утка', 'Кря-Кря')

list_animals = [cows_manya, sheep_barashek, sheep_kudryaviy, goats_roga, goats_kopyta]
list_birds = [geese_gray, geese_white, chicken_koko, chicken_kukareku, chicken_kryakva]
all_animals_list = list_animals + list_birds

def info_animals():
    for animal in all_animals_list:
        print(animal.name)
        print(animal.weight)
        if hasattr(animal, 'type_bird'):
            print(animal.type_bird)
        print(animal.voice)
        print()

def collect_artifacts(*args):
    for animal in all_animals_list:
        if hasattr(animal, 'type_bird'):
            animal.collect_eggs(*args)
        elif isinstance(animal, Cows) or isinstance(animal, Goats):
            animal.collect_milk(*args)
        elif isinstance(animal, Sheep):
            animal.collect_wool(*args)

def feed_animals():
    for animal in all_animals_list:
        animal.feed()

def heaviest():
    max_weight = 0
    name_animals = ''
    for animal in all_animals_list:
        if animal.weight > max_weight:
            max_weight = animal.weight
            name_animals = animal.name
    print(name_animals)

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'l':
            info_animals()
        elif user_input == 'c':
            collect_artifacts()
        elif user_input == 'f':
            feed_animals()
        elif user_input == 'm':
            heaviest()
        elif user_input == 'q':
            break

main()

