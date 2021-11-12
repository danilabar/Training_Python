# Кто самый умный супергерой? Есть API по информации о супергероях. Нужно определить кто самый умный(intelligence)
# из трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name
#
# Токен, который нужно использовать для доступа к API: 2619421814940190.
# Таким образом, все адреса для доступа к API должны начинаться с https://superheroapi.com/api/2619421814940190/.

import requests

superheros = ["Hulk", "Thanos", "Captain America"]


def GetSuperHerointelligence(superhero, token=2619421814940190):

    response = requests.get(
    "https://superheroapi.com/api/" + str(token) + "/search/" + superhero
    )

    response.raise_for_status()
    results = response.json()

    for res in results["results"]:
        if res["name"] != superhero:
            continue
        return res["powerstats"]["intelligence"]


intelhero = 0
intelheroname = ''


for superhero in superheros:
    intel = int(GetSuperHerointelligence(superhero))
    print(f'У {superhero} уровень интеллекта {intel}')
    if intel > intelhero:
        intelhero = intel
        intelheroname = superhero

print(f'Самый умный {intelheroname} с уровнем интеллекта {intelhero}')