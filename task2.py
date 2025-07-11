from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import os
import urllib.parse


class WikipediaBrowser:
    def __init__(self):
        self.driver = self._setup_driver()
        self.current_page = None

    def _setup_driver(self):
        """Настройка браузера Chrome"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Можно убрать для отладки
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        chromedriver_path = self._find_chromedriver()
        service = Service(executable_path=chromedriver_path) if chromedriver_path else Service()

        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def _find_chromedriver(self):
        """Поиск chromedriver в системе"""
        possible_paths = [
            'chromedriver.exe',
            os.path.join(os.path.expanduser('~'), 'chromedriver'),
            'C:/Program Files/chromedriver/chromedriver.exe',
            '/usr/local/bin/chromedriver',
            '/usr/bin/chromedriver'
        ]
        return next((path for path in possible_paths if os.path.exists(path)), None)

    def search(self, query):
        """Поиск статьи с обработкой спецсимволов"""
        encoded_query = urllib.parse.quote(query)
        url = f"https://ru.wikipedia.org/wiki/{encoded_query}"
        self.driver.get(url)
        time.sleep(3)

        if "значения" in self.driver.title.lower():
            try:
                first_option = self.driver.find_element(By.XPATH, "//div[@class='mw-parser-output']/ul/li[1]/a")
                first_option.click()
                time.sleep(3)
            except NoSuchElementException:
                pass

        self.current_page = self.driver.current_url

    def get_article_title(self):
        """Получение заголовка статьи"""
        try:
            return self.driver.find_element(By.ID, "firstHeading").text
        except NoSuchElementException:
            return "Статья не найдена"

    def get_paragraphs(self):
        """Получение параграфов статьи"""
        try:
            content = self.driver.find_element(By.ID, "mw-content-text")
            paragraphs = content.find_elements(By.XPATH,
                                               ".//p[not(ancestor::table) and not(ancestor::div[@class='navbox']) and string-length(text()) > 50]")
            return [p.text for p in paragraphs if p.text.strip()]
        except NoSuchElementException:
            return []

    def get_links(self):
        """Получение внутренних ссылок с улучшенным фильтром"""
        try:
            content = self.driver.find_element(By.ID, "bodyContent")
            links = content.find_elements(By.XPATH,
                                          ".//a[contains(@href, '/wiki/') and not(contains(@href, ':')) and not(contains(@href, '#')) and not(contains(@class, 'image'))]")

            # Фильтруем уникальные ссылки с текстом
            unique_links = {}
            for link in links:
                href = link.get_attribute("href")
                text = link.text.strip()
                if href and text and len(text) > 2 and href not in unique_links:
                    unique_links[href] = text

            return list(unique_links.items())
        except NoSuchElementException:
            return []

    def close(self):
        """Закрытие браузера"""
        self.driver.quit()


def display_links(browser):
    """Функция для отображения и выбора связанных статей"""
    links = browser.get_links()

    if not links:
        print("\nНе найдено связанных статей.")
        input("Нажмите Enter чтобы продолжить...")
        return

    print("\nДоступные связанные статьи:")
    for i, (href, title) in enumerate(links[:15], 1):
        print(f"{i}. {title}")

    while True:
        try:
            choice = input("\nВыберите номер статьи (0 - отмена): ").strip()
            if choice == '0':
                return

            selected_href, selected_title = links[int(choice) - 1]
            print(f"\nПереход к статье: {selected_title}...")
            browser.driver.get(selected_href)
            time.sleep(2)

            # После перехода предлагаем действия
            while True:
                new_title = browser.get_article_title()
                print(f"\nТекущая статья: {new_title}")
                print("1. Читать статью")
                print("2. Показать связанные статьи")
                print("3. Вернуться назад")

                sub_choice = input("Выберите действие (1-3): ").strip()

                if sub_choice == '1':
                    display_paragraphs(browser)
                elif sub_choice == '2':
                    display_links(browser)
                    break
                elif sub_choice == '3':
                    browser.driver.back()
                    time.sleep(2)
                    return
                else:
                    print("Неверный ввод. Попробуйте снова.")

        except (ValueError, IndexError):
            print("Неверный номер. Попробуйте снова.")
        except Exception as e:
            print(f"Ошибка: {e}")
            return


def display_paragraphs(browser):
    paragraphs = browser.get_paragraphs()

    if not paragraphs:
        print("\nНе удалось загрузить текст статьи.")
        input("Нажмите Enter чтобы продолжить...")
        return

    current = 0
    while current < len(paragraphs):
        print(f"\n{paragraphs[current]}\n")
        print(f"Параграф {current + 1} из {len(paragraphs)}")

        if current < len(paragraphs) - 1:
            choice = input("Следующий параграф? (д/н): ").lower()
            if choice != 'д':
                break
        else:
            print("\nКонец статьи.")
            input("Нажмите Enter чтобы продолжить...")
            break
        current += 1


def main():
    print("=== Консольный браузер Wikipedia ===")
    print("Поиск статей и навигация по разделам\n")

    browser = WikipediaBrowser()

    try:
        while True:
            query = input("Введите поисковый запрос (или 'выход' для завершения): ").strip()

            if query.lower() in ('выход', 'exit', 'quit'):
                break

            if not query:
                print("Запрос не может быть пустым!")
                continue

            print("\nИдет поиск статьи...")
            browser.search(query)
            title = browser.get_article_title()

            while True:
                print(f"\nТекущая статья: {title}")
                print("\nМеню:")
                print("1. Читать статью")
                print("2. Показать связанные статьи")
                print("3. Новый поиск")
                print("4. Выход")

                choice = input("Выберите действие (1-4): ").strip()

                if choice == '1':
                    display_paragraphs(browser)
                elif choice == '2':
                    display_links(browser)
                elif choice == '3':
                    break
                elif choice == '4':
                    print("\nЗавершение работы программы...")
                    return
                else:
                    print("Неверный ввод. Попробуйте снова.")

    finally:
        browser.close()
        print("\nРабота программы завершена.")


if __name__ == "__main__":
    main()