import strings
import telebot
import emoji
import time

bot = telebot.TeleBot(strings.token)

@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, strings.text_for_start)


@bot.message_handler(commands=['repo'])
def handle_text(message):
    bot.send_message(message.chat.id, strings.repo)

@bot.message_handler(commands=['menu'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row(f'{emoji.emojize(":framed_picture:")} Cелфи', f'{emoji.emojize(":framed_picture:")} Фото из школы')
    user_markup.row(f'{emoji.emojize(":drum:")} Моё увлечение')
    user_markup.row(f'{emoji.emojize(":old_woman:")} Как объяснить бабушке, что такое GPT?')
    user_markup.row(f'{emoji.emojize(":books:")} Разница между SQL и NoSQL')
    user_markup.row(f'{emoji.emojize(":two_hearts:")} История первой любви')
    user_markup.row(f'{emoji.emojize(":down_arrow:")} Закрыть меню')
    bot.send_message(message.chat.id, 'Меню открыто', reply_markup=user_markup)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)