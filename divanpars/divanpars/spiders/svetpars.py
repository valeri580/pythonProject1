import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Режим без графического интерфейса
options.add_argument('--disable-blink-features=AutomationControlled')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.divan.ru/category/svet"
driver.get(url)

# Улучшенное ожидание с прокруткой страницы
try:
    # Прокрутка для загрузки всех товаров
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Ожидание загрузки товаров
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div._Ud0k'))
    )

    # Сбор данных
    parsed_data = []
    items = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
            price = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')
            url = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            parsed_data.append([name, f"{price} руб.", url])
        except Exception as e:
            print(f"Пропущен товар из-за ошибки: {str(e)}")
            continue

except Exception as e:
    print(f"Ошибка при загрузке страницы: {str(e)}")
finally:
    driver.quit()

# Сохранение в CSV с улучшенным форматированием
with open("divan_svet_final.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)

print(f"Успешно сохранено {len(parsed_data)} товаров в файл divan_svet_improved.csv")

