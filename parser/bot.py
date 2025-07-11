from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import telebot
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import sqlite3

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TOKEN = "7799920386:AAG9QxkEQYiVZY12wlq7IY1TlKJZ18eGVU4"
bot = telebot.TeleBot(TOKEN)

DB_path = "product.db"

def main_menu():
    keyboard = [
        [InlineKeyboardButton("🌤 Показать погоду", callback_data='weather')],
        [InlineKeyboardButton("🛍️ Информация", callback_data='info')]
    ]
    return InlineKeyboardMarkup(keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Я бот, который выдаёт товары с WB!",
        reply_markup=main_menu()
    )


@bot.message_handler(commands=['start'])
def start(message):
    """Обработчик команды /start"""
    try:
        bot.send_message(
            message.chat.id,
            "Я бот, который выдаёт товары с WB!",
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
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Функция погоды в разработке 🛠",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("⬅️ Назад", callback_data='back')]
                ])
            )

        elif call.data == 'info':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="ℹ️ Это учебный бот\nВерсия 1.0",
                reply_markup=main_menu()
            )

        elif call.data == 'back':
            bot.answer_callback_query(call.id)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="Я бот, который выдаёт товары с WB!",
                reply_markup=main_menu()
            )

    except telebot.apihelper.ApiTelegramException as e:
        logger.error(f"Telegram API error: {e}")
        bot.answer_callback_query(call.id, text="Произошла ошибка, попробуйте позже")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        bot.answer_callback_query(call.id, text="Внутренняя ошибка бота")

@bot.message_handler(commands=['product'])
def product(message):
    parts = message.text.split()
    if len(parts) != 2:
        bot.send_message(message.chat.id, "Неверный формат команды! Верный формат - /product 2")
        return

    try:
        product_id = int(parts[1])
    except:
        bot.send_message(message.chat.id, "ID должен быть числом!")
        return

    conn = sqlite3.connect(DB_path)
    c = conn.cursor()
    c.execute("SELECT name, image_path FROM product_list WHERE id = ?", (product_id,))
    result = c.fetchone()
    conn.close()


    if result:
        name, image_path = result
        with open(image_path, "rb") as image:
            bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, name)
    else:
        bot.send_message(message.chat.id, "Результат по данному запросу не был найден")

# Запуск бота
if __name__ == '__main__':
    logger.info("Бот запускается...")
    try:
        bot.polling(none_stop=True, interval=2, timeout=60)
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
    finally:
        logger.info("Работа бота завершена")
