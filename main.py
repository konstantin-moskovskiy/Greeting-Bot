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
    user_markup.row(f'{emoji.emojize(":framed_picture:")} Селфи', f'{emoji.emojize(":framed_picture:")} Фото из школы')
    user_markup.row(f'{emoji.emojize(":drum:")} Моё увлечение')
    user_markup.row(f'{emoji.emojize(":old_woman:")} Как объяснить бабушке, что такое GPT?')
    user_markup.row(f'{emoji.emojize(":books:")} Разница между SQL и NoSQL')
    user_markup.row(f'{emoji.emojize(":two_hearts:")} История первой любви')
    user_markup.row(f'{emoji.emojize(":down_arrow:")} Закрыть меню')
    bot.send_message(message.chat.id, 'Меню открыто', reply_markup=user_markup)

@bot.message_handler(content_types=['text'])    # обработчик текстового сообщения
def handle_text(message):
    if 'Закрыть меню' in message.text:
        hide_markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Меню закрыто', reply_markup=hide_markup)
    elif 'Фото из школы' in message.text:
        bot.send_photo(message.chat.id, open("materials/school_photo.jpg", "rb"))
    elif 'Моё увлечение' in message.text:
        bot.send_message(message.chat.id, strings.story)
    elif 'Как объяснить бабушке, что такое GPT?' in message.text:
        bot.send_audio(message.chat.id, open("materials/GPT.mp3", "rb"))
    elif 'Разница между SQL и NoSQL' in message.text:
        bot.send_audio(message.chat.id, open("materials/SQL.mp3", "rb"))
    elif 'История первой любви' in message.text:
        bot.send_audio(message.chat.id, open("materials/LOVE.mp3", "rb"))
    elif 'Селфи' in message.text:
        bot.send_photo(message.chat.id, open("materials/selfie.jpg", "rb"))
    else:
        bot.send_message(message.chat.id, strings.oops)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(15)