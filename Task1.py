import telebot
import random
import requests
from bs4 import BeautifulSoup


# Токен бота
TOKEN = '8136343436:AAHjqtXn68_tTkQeBLzx25LCg_l5gFr-770'

bot = telebot.TeleBot(TOKEN)

# Список блюд для случайного выбора
dishes = [
    "Пицца Маргарита",
    "Спагетти Карбонара",
    "Салат Цезарь",
    "Стейк Рибай",
    "Суши Филадельфия",
    "Борщ",
    "Пельмени",
    "Паста Болоньезе",
    "Рамен",
    "Греческий салат",
    "Бургер с сыром",
    "Том Ям"
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой тестовый бот. Вот что я умею:\n"
                          "/start - приветственное сообщение\n"
                          "/random_dish - случайное блюдо\n"
                          "Также я могу анализировать текст и отвечать на ключевые слова.")


# Обработчик команды /random_dish
@bot.message_handler(commands=['random_dish'])
def send_random_dish(message):
    dish = random.choice(dishes)
    bot.reply_to(message, f"Я рекомендую вам попробовать: {dish}")

# Обработчик команды /news
@bot.message_handler(commands=['news'])
def send_news(message):
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
                    bot.send_message(message.chat.id, f"{i + 1}. {title_div.text.strip()} \n Ссылка: {link}")
                else:
                    bot.send_message(message.chat.id, f"{i + 1}. {title_div.text.strip()} \n Ссылка не найдена")
    else:
        print(f"Ошибка при загрузке страницы {response.status_code}")
        bot.send_message(message.chat.id, "Не удалось получить данные о новостях в Томске!")


# Обработчик всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # Пропускаем команды
    if message.text.startswith('/'):
        return

    # Пропускаем пустые сообщения
    if not message.text:
        return

    text = message.text.lower()
    if 'привет' in text:
        bot.reply_to(message, "Привет! Как дела?")
    elif 'пока' in text:
        bot.reply_to(message, "До свидания! Возвращайся скорее!")
    elif 'спасибо' in text:
        bot.reply_to(message, "Пожалуйста! Рад помочь!")
    elif 'как дела' in text:
        bot.reply_to(message, "У меня все отлично! А у тебя?")
    elif 'счет' in text or 'посчитать' in text:
        count_stats(message)
    else:
        bot.reply_to(message, "Я получил твое сообщение: " + message.text)
        count_stats(message)


# Функция для подсчета статистики текста
def count_stats(message):
    text = message.text
    words = len(text.split())
    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", ""))

    response = (f"Статистика вашего сообщения:\n"
                f"Слов: {words}\n"
                f"Символов (с пробелами): {chars_with_spaces}\n"
                f"Символов (без пробелов): {chars_without_spaces}")

    bot.reply_to(message, response)


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)