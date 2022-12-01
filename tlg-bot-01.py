from flask import Flask, request
import telebot
import os

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message.handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello, user!')

@bot.message.handler(commands=['Links'])
def message_courses(message):
    keyboard = telebot.types.InLineKeyboardMarkup(row_width=1)

    with open('Links.txt') as file:
        links = [item.split(',') for item in file]

        for title. link in links:
            url_button = telebot.types.InLineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send.message(message.chat.id, 'List of links', reply_markup=keyboard)

@bot.message.handler(func=lambda x: x.text.lower().startwith('Not interested'))
def message_text(message):
    bot.send.message(message.chat.id, 'If you`ll change your mind - please, chat again')

@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Python Telegram Bot", 200

@app.route('/')
def main():
    bot.remove_webhook()
    bot.set_webhook(url='https://tlg-bot-01.herokuapp.com/' + TOKEN)
    return 'Python Telegram Bot', 200

if __name__ == '__tlg-bot-01__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
