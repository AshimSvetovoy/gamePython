import telebot
import random
from telebot import types
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.getenv("API_TOKEN"))
answer_poll = ['Rock', 'Scissors', 'Papper']
#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    print(message)
#    bot.reply_to(message, message.text)

#@bot.message_handler(content_types=['photo'])
#def photo_callback(message):
#    bot.reply_to(message, "Вау да это же фото, кто бы мог подумать")

# greetings = ["Дарова", "Ты хто такой?", "hello", "Привет"]
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if (message.text in greetings):
#         bot.reply_to(message, "Привет")
@bot.message_handler(commands=['game'])
def game_reply(message):
    # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # itembtn1 = types.KeyboardButton('1')
    # itembtn2 = types.KeyboardButton('2')
    # itembtn3 = types.KeyboardButton('3')

    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton(text='Камень', callback_data='Rock')
    itembtn2 = types.InlineKeyboardButton(text='Ножницы', callback_data='Scissors')
    itembtn3 = types.InlineKeyboardButton(text='Бумага', callback_data='Papper')
    itembtn4 = types.InlineKeyboardButton(text='Заново', callback_data='Again')


    markup.row(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выбери пжпжпжпжжпжппж", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def answering(call):
    if call.data == "Again":
        game_reply(call.message)
        return


    bot_answer = answer_poll[random.randint(0, 2)]
    bot.send_message(call.message.chat.id, bot_answer)
    result = answer_poll.index(call.data) - answer_poll.index(bot_answer)
    if result == -1 or result == 2:
        bot.send_message(call.message.chat.id, "Ты выйграл")
    elif result == 0:
        bot.send_message(call.message.chat.id, "Ничья")
    else:
        bot.send_message(call.message.chat.id, "Я выйграл")





bot.infinity_polling()