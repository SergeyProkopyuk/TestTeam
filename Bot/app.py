import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите комманду боту в следующем формате:\n<имя валюты цену которой вы хотите узнать> \
<имя валюты в которой надо узнать цену первой валюты> \
<количество первой валюты>\nВалюты нужно писать в именительном падеже, в единственном числе. \
\nНапример - доллар рубль 10 \
\nУвидеть список доступных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(" ")

        if len(values) != 3:
            raise APIException("Слишком много параметров.")

        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду.\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} - {round(total_base, 2)}"
        bot.send_message(message.chat.id, text)

bot.polling()