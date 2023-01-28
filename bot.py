import telebot
import config
from telebot import types

settings = config.Configurator()
tbot = telebot.TeleBot(token=settings.token)
current_markup = telebot.types.ReplyKeyboardMarkup()
monitoring = False


def send(text: str = "", photo_path: str = "", reply_markup=None,
         chat_id: str = settings.chat_id):
    tbot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
    if photo_path:
        tbot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))


def apply_menu(menu):
    global current_markup
    current_markup = menu
    send(text='Menu:', reply_markup=menu)


def get_menu(buttons: list, markup_type=None, back_button=False):
    from Buttons import Buttons
    markup = types.InlineKeyboardMarkup() if markup_type is types.InlineKeyboardMarkup \
        else types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(button)
    if back_button:
        markup.add(Buttons.back)
    return markup
