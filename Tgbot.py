import pip
pip.main(['install', 'pyTelegramBotAPI'])

import telebot

bot = telebot.TeleBot("883839412:AAHfWuR_GRdScflyUx94YgV8926aNEc_6Sk")

@bot.message_handler(content_types = ['text'])
def send_welcome(message):
   # bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, message.text)
    
bot.polling( none_stop = True )
