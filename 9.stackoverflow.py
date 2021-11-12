# Самый важный сайт для программистов это stackoverflow https://stackoverflow.com/.
# И у него тоже есть API https://api.stackexchange.com/docs
# Нужно написать программу, которая выводит все вопросы за последние два дня и содержит
# тэг 'Python'. Для этого задания токен не требуется.

# https://api.stackexchange.com/2.3/questions?fromdate=1636243200&todate=1636416000&order=desc&sort=creation&tagged=python&site=stackoverflow
import datetime
from pprint import pprint

import requests


current_date = datetime.date.today()
past_date = current_date - datetime.timedelta(days=2)

resp = requests.get(
    "https://api.stackexchange.com/2.3/questions",
    params={"fromdate": past_date,
            "todate": current_date,
            "order": "desc",
            "sort": "creation",
            "tagged": "python",
            "site": "stackoverflow"
            }
)

resp.raise_for_status()
data = resp.json()
# pprint(data)

for file in data["items"]:
    print(f'Дата поста :{datetime.date.fromtimestamp(file["creation_date"])}')
    print(f'Теги поста :{file["tags"]}')
    print(f'Имя поста :{file["title"]}')
    print()