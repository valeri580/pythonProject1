import requests
from bs4 import BeautifulSoup
import sqlite3

from soupsieve.css_parser import VALUE

conn = sqlite3.connect('news.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS news (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            link TEXT
)
 ''')

conn.commit()

# lenta_material_title
url = "https://vtomske.ru/"
response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('div', class_="lenta_material_title", limit=5)

    for i in range(len(titles)):  # 0, 1, 2, 3, 4
        title_div = titles[i]
        a_tag = title_div.find_parent('a', class_="lenta_material")
        if a_tag and a_tag.has_attr("href"):
            link = a_tag["href"]
            if link.startswith("/"):
                link = url.rstrip("/") + link

            cursor.execute("INSERT INTO news (title, link) VALUES (?, ?)", (title_div.text.strip(),link))
            conn.commit()
            print(f"{i + 1}. {title_div.text.strip()} \n Ссылка: {link}")
        else:
            print(f"{i + 1}. {title_div.text.strip()} \n Ссылка не найдена")
else:
    print(f"Ошибка при загрузке страницы {response.status_code}")

conn.close()

