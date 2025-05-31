import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("7896525238:AAFQckqtj0whgFUMCgZXRg5UEeJ9Xlv3Ja8")

user_data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить водичку!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = [
        "**Вода на нашей Земле может быть старше самой Солнечной системы**: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
        "**Горячая вода замерзает быстрее холодной**: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
        "**Больше воды в атмосфере, чем во всех реках мира**: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде {random_fact}')

@bot.message_handler(commands=['help'])
def help_message(message):
    descriptions = {
        '/start': 'Запуск бота и приветственное сообщение.',
        '/fact': 'Получите интересный факт.',
        '/help': 'Показать список доступных команд и их описания.',
        '/set_reminder': 'Установите напоминание о важном событии.',
        '/log_water': 'Запишите количество выпитой воды.',
        '/set_goal': 'Установите личную цель.',
        '/motivate': 'Получите мотивационное сообщение для повышения настроения.'
    }

    help_text = "В боте доступно 6 функций:\n"
    for command, description in descriptions.items():
        help_text += f"{command}: {description}\n"

    bot.reply_to(message, help_text)

@bot.message_handler(commands=['set_reminder'])
def set_reminder(message):
    try:
        times = message.text.split()[1].split(',')
        user_data[message.chat.id] = {'reminders': times, 'goal': 2000, 'logged_water': 0}
        bot.reply_to(message, f'Напоминания установлены на: {", ".join(times)}')
    except IndexError:
        bot.reply_to(message, 'Пожалуйста, укажите время напоминаний в формате: /set_reminder 09:00,14:00,18:00')

@bot.message_handler(commands=['log_water'])
def log_water(message):
    try:
        amount = int(message.text.split()[1].replace('ml', ''))
        user_data[message.chat.id]['logged_water'] += amount
        bot.reply_to(message, f'Добавлено {amount}ml к вашему дневному количеству. Всего: {user_data[message.chat.id]["logged_water"]}ml.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, укажите количество воды в миллилитрах: /log_water 250ml')

@bot.message_handler(commands=['set_goal'])
def set_goal(message):
    try:
        goal = int(message.text.split()[1].replace('ml', ''))
        user_data[message.chat.id]['goal'] = goal
        bot.reply_to(message, f'Ваша дневная цель установлена на {goal}ml.')
    except (IndexError, ValueError):
        bot.reply_to(message, 'Пожалуйста, укажите вашу цель в миллилитрах: /set_goal 2000ml')

@bot.message_handler(commands=['motivate'])
def motivate(message):
    motivations = [
        "Продолжайте, в том же духе, ваше здоровье скажет вам спасибо!",
        "Каждый стакан воды приближает вас к здоровой жизни!",
        "Вы великолепны! Не забывайте пить воду!" ]
    bot.reply_to(message, random.choice(motivations))

def send_reminders(chat_id):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if chat_id in user_data:
            for reminder_time in user_data[chat_id]['reminders']:
                if now == reminder_time:
                    bot.send_message(chat_id, "Напоминание - выпей стакан воды")
        time.sleep(60)
        time.sleep(1)

bot.polling(none_stop=True)







