from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Без окна браузера (по желанию)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

prices = []
names = []

for page in range(1, 4):
    url = f"https://www.divan.ru/category/divany?page={page}"
    print(f"Парсим {url}")
    driver.get(url)
    time.sleep(3)  # Ждём подгрузки JS

    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all("div", class_="lsooF")

    for item in items:
        name_tag = item.find("div", class_="lsooF")
        name = name_tag.text.strip() if name_tag else "Без названия"

        price_tag = item.find("meta", itemprop="price")
        if price_tag:
            price = price_tag.get("content")
        else:
            price_text = item.text
            price_match = re.search(r"(\d[\d\s]+)₽", price_text)
            price = price_match.group(1).replace(" ", "") if price_match else None

        if price and price.isdigit():
            prices.append(int(price))
            names.append(name)
    time.sleep(1)

driver.quit()

df = pd.DataFrame({"Название": names, "Цена": prices})
df.to_csv("divan_prices.csv", index=False, encoding="utf-8-sig")

print(f"Найдено {len(prices)} цен")
if prices:
    average_price = sum(prices) / len(prices)
    print(f"Средняя цена: {average_price:.2f} руб.")
    plt.hist(prices, bins=20, edgecolor="black", alpha=0.7)
    plt.title("Гистограмма цен на диваны с divan.ru")
    plt.xlabel("Цена, руб.")
    plt.ylabel("Количество")
    plt.grid(True)
    plt.show()
else:
    print("Нет данных для построения гистограммы.")
