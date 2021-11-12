import os
from pprint import pprint

import requests

GIFS_DIR = "gifs"

response = requests.get(
    "https://www.reddit.com/r/gifs.json",
    headers={"User-Agent": "netology"}
)
if response.status_code != 200:
    raise Exception("всё очень плохо")
# response.raise_for_status() - можно заменить условие выше
posts = response.json()["data"]["children"]

for post in posts:
    title: str = post["data"]["title"]
    url = post["data"]["url"]
    if "imgur.com/" not in url:
        continue
    url = url.replace(".gifv", ".gif")

    gif_resp = requests.get(url)
    gif_resp.raise_for_status()

    title = "".join(x for x in title if x.isalnum() or x.isspace())

    with open(os.path.join(GIFS_DIR, title + ".gif"), "wb") as f:
        f.write(gif_resp.content)
        print(title)


# --------------

# получить список файлов на яндекс диске
HEADERS = {"Autorization": "OAuth dsfdfsewfwwebfwbdw"}

resp = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources",
    params={"path": "/"},
    headers=HEADERS,
)
resp.raise_for_status()
data = resp.json()

for file in data['_embedded']["items"]:
    print(file["name"])

# Получить ссылку на загрузку файлов на яндекс диск

resp1 = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources/upload",
    params={"path": "/awesome.gif", "overwrite": "true"},
    headers=HEADERS,
)

resp1.raise_for_status()
d = resp1.json()
# pprint(d) # получили ссылку href и метод PUT
href = d["href"]

# Отправляем файл

with open("gifs/ddfd.gif", "rb") as f:
    resp2 = requests.put(href, files={"file": f})

resp2.raise_for_status()