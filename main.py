import telebot as tb
import random

bot = tb.TeleBot('7165362808:AAG3ri19R7ly9DBMvPwoayFD8Vt5I0CrTS4')



@bot.message_handler(commands=['go'])
def go(message: tb.types.Message):
    bot.send_message(message.chat.id, 'Введите варианты для выбора в следующем формате:')
    bot.send_message(message.chat.id, '1. Вариант_1\n2. Вариант_2\n3. Вариант_3')


@bot.message_handler(commands=['start'])
def start(message: tb.types.Message):
    bot.send_message(message.chat.id, '/go - начать')


@bot.message_handler(content_types=['text'])
def choice(message: tb.types.Message):
    mess = message.text.split('\n')
    r = random.randint(1, len(mess))
    bot.send_message(message.chat.id, f"Советуем Вам выбрать вариант номер {r}: {mess[r - 1][2:]}")


bot.infinity_polling()
