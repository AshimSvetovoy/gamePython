import telebot
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot = telebot.TeleBot(os.getenv("API_TOKEN"))

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    print(message)
#    bot.reply_to(message, message.text)

#@bot.message_handler(content_types=['photo'])
#def photo_callback(message):
#    bot.reply_to(message, "Вау да это же фото, кто бы мог подумать")

greetings = ["Дарова", "Ты хто такой?", "hello", "Привет"]
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if (message.text in greetings):
        bot.reply_to(message, "Привет")


bot.infinity_polling()