import requests
import telebot
import logging
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

# Настройка логгирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Загрузка переменных окружения
load_dotenv()

# Константы
VALERIADMIN_TG_BOT_API_KEY = os.getenv("VALERIADMIN_TG_BOT_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CBR_API_URL = "https://www.cbr-xml-daily.ru/daily_json.js"

# Инициализация бота
bot = telebot.TeleBot(VALERIADMIN_TG_BOT_API_KEY)


def main_menu():
    keyboard = [
        [InlineKeyboardButton("🌤 Погода", callback_data='weather'),
         InlineKeyboardButton("💱 Курсы валют", callback_data='currency')],
        [InlineKeyboardButton("ℹ️ Информация", callback_data='info')]
    ]
    return InlineKeyboardMarkup(keyboard)


def back_to_menu():
    keyboard = [
        [InlineKeyboardButton("🔙 Назад в меню", callback_data='back')]
    ]
    return InlineKeyboardMarkup(keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start"""
    try:
        bot.send_message(
            message.chat.id,
            "Я бот, который выдаёт курсы валют и погоду!",
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в start: {e}", exc_info=True)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    """Обработчик нажатий на inline-кнопки"""
    try:
        if call.data == 'weather':
            bot.answer_callback_query(call.id)
            msg = bot.send_message(
                call.message.chat.id,
                "Введите название города:",
                reply_markup=back_to_menu()
            )
            bot.register_next_step_handler(msg, process_weather_city)

        elif call.data == 'currency':
            bot.answer_callback_query(call.id)
            show_currency_rates(call.message)

        elif call.data == 'info':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="ℹ️ Это учебный бот\nВерсия 2.0",
                reply_markup=main_menu()
            )

        elif call.data == 'back':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Я бот, который выдаёт курсы валют и погоду!",
                reply_markup=main_menu()
            )

    except Exception as e:
        logger.error(f"Ошибка в callback_handler: {e}", exc_info=True)
        bot.answer_callback_query(call.id, text="Произошла ошибка, попробуйте позже")


def process_weather_city(message):
    """Обработка ввода города для погоды"""
    try:
        city = message.text
        weather_data = get_weather(city)

        if weather_data == 404:
            msg = bot.send_message(
                message.chat.id,
                "Город не найден. Попробуй ещё раз:",
                reply_markup=back_to_menu()
            )
            bot.register_next_step_handler(msg, process_weather_city)
            return

        if weather_data:
            response = (f"Погода в {city}:\n"
                        f"Температура: {round(weather_data['temp'], 1)}°C\n"
                        f"Ощущается как: {round(weather_data['feels_like'], 1)}°C\n"
                        f"Влажность: {weather_data['humidity']}%\n"
                        f"Описание: {weather_data['description']}")
        else:
            response = "Не удалось получить данные о погоде"

        bot.send_message(
            message.chat.id,
            response,
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в process_weather_city: {e}", exc_info=True)
        bot.send_message(message.chat.id, "Произошла ошибка при обработке запроса")


def get_weather(city):
    """Получение данных о погоде"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ru"
        response = requests.get(url)

        if response.status_code == 404:
            return 404

        data = response.json()

        if response.status_code == 200:
            return {
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
        return None
    except Exception as e:
        logger.error(f"Ошибка в get_weather: {e}", exc_info=True)
        return None


def show_currency_rates(message):
    """Показать курсы валют"""
    try:
        rates = get_currency_rates()
        if rates:
            response = (f"Курсы валют ЦБ РФ:\n"
                        f"🇺🇸 USD: {rates['USD']} руб.\n"
                        f"🇪🇺 EUR: {rates['EUR']} руб.\n"
                        f"🇨🇳 CNY: {rates['CNY']} руб.")
        else:
            response = "Не удалось получить курсы валют"

        bot.send_message(
            message.chat.id,
            response,
            reply_markup=main_menu()
        )
    except Exception as e:
        logger.error(f"Ошибка в show_currency_rates: {e}", exc_info=True)
        bot.send_message(message.chat.id, "Произошла ошибка при получении курсов валют")


def get_currency_rates():
    """Получение курсов валют от ЦБ РФ"""
    try:
        response = requests.get(CBR_API_URL)
        data = response.json()

        return {
            'USD': round(data['Valute']['USD']['Value'], 2),
            'EUR': round(data['Valute']['EUR']['Value'], 2),
            'CNY': round(data['Valute']['CNY']['Value'], 2)
        }
    except Exception as e:
        logger.error(f"Ошибка в get_currency_rates: {e}", exc_info=True)
        return None


if __name__ == '__main__':
    logger.info("Бот запущен")
    bot.polling(none_stop=True)