import telebot
from telebot import types
import aiohttp
import asyncio
from src.fetching import Fetch

bot = telebot.TeleBot('6761059320:AAFRt3IphHjasUagnz8ArxkQA7pLb-9jZAo')


class UserState:
    def __init__(self):
        self.user_tags = []
        self.tag_user = ""


user_state = UserState()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id

    asyncio.run(Fetch.registrate_user(user_id))
    tags = asyncio.run(Fetch.tags())

    user_state.user_tags = tags

    markup = types.InlineKeyboardMarkup()
    for tag in tags:
        markup.add(types.InlineKeyboardButton(text=tag, callback_data=tag))

    bot.reply_to(message, "выберите тег, который вас интересует")


@bot.message_handler(func=lambda message: True)
def group(message):
    group_show = asyncio.run(Fetch.group(user_state.tag_user))
    group_show["images"] = list(map(lambda image: types.InputMediaPhoto(image, caption=message.caption), group_show["images"]))

    buttons = [{
        "text": "next",
        "callback_data": "skip",
    }, {
        "text": "alert",
        "callback_data": group_show.get("id"),
    }, {
        "text": "interested",
        "callback_data": group_show.get("id"),
    },
    ]

    markup = types.InlineKeyboardMarkup()
    markup.add(*map(lambda button: types.InlineKeyboardButton(text=button.get("text"), callback_data=button.get("callback_data")), buttons))

    bot.send_media_group(message.chat.id, group_show.get("images"))
    bot.send_message(message.chat.id, group_show.get("description"))


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    asyncio.run(Fetch.add_tag_user(call.data))


bot.polling()
