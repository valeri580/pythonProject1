import requests # Для отправки HTTP-запросов к внешним API
import logging  # Для настройки системы логирования
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
from dotenv import load_dotenv
import os
import time  # Для замера времени выполнения операций
import uuid


load_dotenv()
VALERIADMIN_TG_BOT_API_KEY = os.getenv("VALERIADMIN_TG_BOT_API_KEY")
YANDEX_API_KEY = os.getenv("YANDEX_API_KEY")
YANDEX_FOLDER_ID = os.getenv("YANDEX_FOLDER_ID")
AUTHORIZATION_KEY = os.getenv("AUTHORIZATION_KEY")


url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
cert_path = "C:/Users/valeri/PycharmProjects/pythonProject1/.venv/Lib/site-packages/certifi/cacert.pem.cer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ers\valeri\OneDrive\Рабочий стол\sert.cer"  # например, "sberbank_ca.pem"
payload={
  'scope': 'GIGACHAT_API_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': 'f4d6f258-88ac-48d9-a13d-d10d59f972e5',
  'Authorization': 'Basic AUTHORIZATION_KEY'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=cert_path)

print(response.text)


# Настройка системы логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Формат записи логов
    level=logging.INFO  # Уровень логирования (INFO и выше)
)
# Создание логгера для текущего модуля
logger = logging.getLogger(__name__)

class RussianAI:
    # Конструктор класса
    def __init__(self):
        self.provider = os.getenv("DEFAULT_PROVIDER", "yandexgpt") # Получение провайдера по умолчанию из переменных окружения
        self.conversation_history = [] # Инициализация истории диалога как пустого списка
        self.set_provider(self.provider)# Настройка выбранного провайдера

    def set_provider(self, provider: str):
        self.provider = provider.lower()  # Название провайдера переводим в нижний регистр
        self.conversation_history = []# Сброс истории диалога при смене провайдера

        if self.provider == "yandexgpt":  # Настройка параметров для YandexGPT
            self.api_key = os.getenv("YANDEX_API_KEY")# Получение API-ключа из переменных окружения
            self.folder_id = os.getenv("YANDEX_FOLDER_ID") # Получение идентификатора каталога Yandex Cloud
            self.model = os.getenv("YANDEX_MODEL", "yandexgpt-lite")# Получение модели (по умолчанию "yandexgpt-lite")
            self.base_url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion" # URL API YandexGPT

            if not self.api_key or not self.folder_id:  # Проверка наличия обязательных ключей
                logger.error("Не заданы YANDEX_API_KEY и YANDEX_FOLDER_ID")# Запись ошибки в лог
                return False  # Возврат статуса ошибки

        elif self.provider == "sberai":# Настройка параметров для SberAI (GigaChat)
            self.api_key = os.getenv("SBER_API_KEY")  # Получение API-ключа SberAI
            self.model = os.getenv("SBER_MODEL", "GigaChat:latest")   # Получение модели (по умолчанию "GigaChat:latest")
            self.base_url = "https://api.gigachat.dev/v1/chat/completions"    # URL API SberAI

            if not self.api_key:     # Проверка наличия API-ключа
                logger.error("Не задан SBER_API_KEY")
                return False

        else:
            logger.error(f"Неизвестный провайдер: {provider}")  # Обработка неизвестного провайдера
            return False

        logger.info(f"Используется провайдер: {self.provider.upper()} ({self.model})") # Запись информации о выбранном провайдере в лог
        return True  # Успешное завершение настройки

    # Метод для добавления сообщения в историю диалога
    def add_message(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})

    # Основной метод для генерации ответа на пользовательский ввод
    def generate_response(self, user_input: str):
        self.add_message("user", user_input)
        try:
            # Выбор соответствующего метода API в зависимости от провайдера
            if self.provider == "yandexgpt":
                return self._yandex_request()
            elif self.provider == "sberai":
                return self._sber_request()

        except Exception as e:
            return f"🚨 Ошибка API ({self.provider}): {str(e)}"

    # Приватный метод для работы с API YandexGPT
    def _yandex_request(self):
        headers = {
            "Authorization": f"Api-Key {self.api_key}",  # API-ключ для аутентификации
            "Content-Type": "application/json",  # Тип содержимого
            "x-folder-id": self.folder_id  # Идентификатор каталога
        }
        yandex_messages = []
        for msg in self.conversation_history:
            yandex_messages.append({
                "role": msg["role"],
                "text": msg["content"]  # Yandex использует "text" вместо "content"
            })
            # Формирование тела запроса (payload)
            payload = {
                "modelUri": f"gpt://{self.folder_id}/{self.model}",  # URI модели
                "completionOptions": {
                    "stream": False,  # Режим без потоковой передачи
                    "temperature": 0.7,  # Креативность ответов
                    "maxTokens": 2000  # Максимальное количество токенов в ответе
                },
                "messages": yandex_messages  # История диалога
            }
            try:
                response = requests.post(
                    self.base_url,  # URL API
                    headers=headers,  # Заголовки
                    json=payload,  # Тело запроса в формате JSON
                    timeout=30  # Таймаут запроса (30 секунд)
                )
                # Проверка статуса ответа
                if response.status_code != 200:
                    # Логирование ошибки при ненормальном статусе
                    logger.error(f"Ошибка {response.status_code}: {response.text}")
                    return f"Ошибка API: {response.text}"

                data = response.json()
                ai_reply = data["result"]["alternatives"][0]["message"]["text"]
                self.add_message("assistant", ai_reply)
                return ai_reply  # Возврат сгенерированного ответа

            except Exception as e:
                return f"Ошибка соединения: {str(e)}"

    # Приватный метод для работы с API GIGACHAT
    def _sber_request(self):
        auth_response = requests.post(
            "https://api.gigachat.dev/v1/oauth/token",  # URL для аутентификации
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
                "assertion": self.api_key,  # Использование API-ключа в качестве JWT
                "scope": "GIGACHAT_API_PERS"  # Область доступа
            }
        )
        if auth_response.status_code != 200:
            logger.error(f"Ошибка аутентификации SberAI: {auth_response.text}")
            return "Ошибка аутентификации SberAI"

        auth_data = auth_response.json()
        # Получение токена доступа
        access_token = auth_data["access_token"]
        headers = {
            "Authorization": f"Bearer {access_token}",  # Использование токена доступа
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,  # Идентификатор модели
            "messages": self.conversation_history,  # История диалога
            "temperature": 0.7,  # Креативность ответов
            "max_tokens": 2000  # Максимальное количество токенов в ответе
        }

        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            logger.error(f"Ошибка SberAI: {response.status_code} - {response.text}")
            return f"Ошибка SberAI: {response.text}"

        data = response.json()
        ai_reply = data["choices"][0]["message"]["content"]
        self.add_message("assistant", ai_reply)
        return ai_reply

    def clear_history(self):
        self.conversation_history = []
        logger.info("История диалога очищена")  # Логирование события
        return True  # Подтверждение успешного выполнения

ai_assistant = RussianAI()

def start(update: Update, context: CallbackContext) -> None:
    help_text = (
        "🤖 Привет! Я российский AI-ассистент. Могу ответить на ваши вопросы с помощью:\n"
        f"• YandexGPT ({ai_assistant.model if ai_assistant.provider == 'yandexgpt' else 'доступен через /yandex'})\n"
        f"• SberAI ({ai_assistant.model if ai_assistant.provider == 'sberai' else 'доступен через /sber'})\n\n"
        "Доступные команды:\n"
        "/yandex - использовать YandexGPT\n"
        "/sber - использовать SberAI (GigaChat)\n"
        "/clear - очистить историю диалога\n\n"
        "Просто отправьте мне сообщение с вашим вопросом!")

    keyboard = [
        [KeyboardButton("/yandex"), KeyboardButton("/sber")],
        [KeyboardButton("/clear")]
    ]

    update.message.reply_text(
        help_text,
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
            one_time_keyboard=False
        )
    )


def switch_to_yandex(update: Update, context: CallbackContext) -> None:
    if ai_assistant.set_provider("yandexgpt"):
        update.message.reply_text(
            f"✅ Переключено на YandexGPT ({ai_assistant.model})",
            reply_markup=create_keyboard()  # Обновление клавиатуры
        )
    else:
        update.message.reply_text("❌ Не удалось переключиться на YandexGPT")


def switch_to_sber(update: Update, context: CallbackContext) -> None:
    if ai_assistant.set_provider("sberai"):
        update.message.reply_text(
            f"✅ Переключено на SberAI ({ai_assistant.model})",
            reply_markup=create_keyboard()  # Обновление клавиатуры
        )
    else:
        update.message.reply_text("❌ Не удалось переключиться на SberAI")

def clear_history(update: Update, context: CallbackContext) -> None:
    if ai_assistant.clear_history():
        update.message.reply_text(
            "🗑️ История диалога очищена!",
            reply_markup=create_keyboard()  # Обновление клавиатуры
        )
    else:
        update.message.reply_text("❌ Не удалось очистить историю")

def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    if user_input.startswith('/'):
        return
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing"
    )    # ID текущего чата
    start_time = time.time()
    try:
        response = ai_assistant.generate_response(user_input)
        elapsed_time = time.time() - start_time

        formatted_response = (
        f"🤖 {ai_assistant.provider.upper()} отвечает:\n\n"
        f"{response}\n\n"
        f"⏱ Время генерации: {elapsed_time:.2f} сек"
        )

        update.message.reply_text(
        formatted_response,
        reply_markup=create_keyboard()  # Отправка с клавиатуры команд
        )

    except Exception as e:
        logger.error(f"Ошибка генерации ответа: {str(e)}")
        update.message.reply_text(
            "🚨 Произошла ошибка при генерации ответа. Попробуйте позже.",
            reply_markup=create_keyboard()
        )


def create_keyboard():
    keyboard = [
        [KeyboardButton("/yandex"), KeyboardButton("/sber")],
        [KeyboardButton("/clear")]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
def main():
    if not os.getenv("YANDEX_API_KEY") and not os.getenv("SBER_API_KEY"):
        logger.error("Не найдены API-ключи! Проверьте .env файл")
        print("❌ ОШИБКА: Не найден ни один API ключ в .env файле!")
        print("Добавьте ключи для Yandex или SberAI")
        print("Пример .env файла:")
        print("YANDEX_API_KEY=ваш_ключ_яндекс")
        print("YANDEX_FOLDER_ID=ваш_folder_id")
        print("SBER_API_KEY=ваш_ключ_сбер")
        return  # Завершение работы при отсутствии ключей

    TOKEN = os.getenv("VALERIADMIN_TG_BOT_API_KEY")

    if not TOKEN:
        logger.error("Не задан TELEGRAM_BOT_TOKEN в .env файле!")
        print("❌ ОШИБКА: Не задан TELEGRAM_BOT_TOKEN в .env файле!")
        return

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("yandex", switch_to_yandex))
    dispatcher.add_handler(CommandHandler("sber", switch_to_sber))
    dispatcher.add_handler(CommandHandler("clear", clear_history))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()

    logger.info("🤖 Российский AI-ассистент запущен и готов к работе!")
    print("Бот успешно запущен. Используйте /start в Telegram для начала работы.")
    updater.idle()

if __name__ == '__main__':
    main()
