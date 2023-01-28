import telebot
from monitoring import MonitoringBot
from Buttons import Buttons
import bot

__settings_to_change = [0, '']

monitoring_bot = MonitoringBot()

time_frame_intervals = {'m': Buttons.set_buttons([1, 5, 15]),
                        'H': Buttons.set_buttons([1, 4]),
                        'Dutc': Buttons.set_buttons([1, 2, 3])}

start_menu = bot.get_menu(buttons=[Buttons.start_monitoring,
                                   Buttons.settings],
                          markup_type=telebot.types.InlineKeyboardMarkup)

stop_menu = bot.get_menu(buttons=[Buttons.stop_monitoring,
                                  Buttons.settings],
                         markup_type=telebot.types.InlineKeyboardMarkup)

setting_menu = bot.get_menu([Buttons.limit_bars,
                             Buttons.relative_price_change,
                             Buttons.time_frame])

time_frame_intervals_menu = bot.get_menu(Buttons.set_buttons([buttons for buttons in time_frame_intervals.keys()]),
                                         back_button=True)


# noinspection PyUnusedLocal
@bot.tbot.message_handler(commands=['stop'])
def stop(message):
    if bot.monitoring:
        monitoring_bot.stop()


# noinspection PyUnusedLocal
@bot.tbot.message_handler(commands=['start', 'settings'])
def start(message):
    bot.apply_menu(menu=start_menu if not bot.monitoring else stop_menu)


@bot.tbot.callback_query_handler(func=lambda call: True)
def control(call):
    if call.data == 'START' and not bot.monitoring:
        bot.send(text='Starting monitoring')
        monitoring_bot.start()
    elif call.data == 'STOP' and bot.monitoring:
        monitoring_bot.stop()
        bot.send(text='Stopping monitoring')
    elif call.data == 'OPEN_SETTINGS':
        bot.apply_menu(menu=setting_menu)


def save_settings(settings_list: list):
    global monitoring_bot
    if bot.monitoring:
        monitoring_bot.stop()
    if settings_list[1] == 'limit_bars':
        bot.settings.set_configurations(limit_bars=settings_list[0])
    elif settings_list[1] == 'relative_price_change':
        bot.settings.set_configurations(relative_price_change=settings_list[0])
    else:
        bot.settings.set_configurations(time_frame=(settings_list[0], settings_list[1]))
    bot.send(text='Settings applied')


@bot.tbot.message_handler(content_types=['text'])
def set_settings(message):
    global __settings_to_change

    if message.text == 'Time frame':
        bot.apply_menu(time_frame_intervals_menu)
        bot.send(text='Time frame change')
    elif message.text in time_frame_intervals.keys():
        markup = bot.get_menu(time_frame_intervals[message.text],
                              markup_type=telebot.types.ReplyKeyboardMarkup,
                              back_button=True)
        __settings_to_change[1] = message.text
        bot.apply_menu(menu=markup)
    elif message.text == "Back":
        if bot.current_markup == time_frame_intervals_menu:
            bot.send(text='Settings', reply_markup=setting_menu)
        else:
            bot.current_markup = time_frame_intervals_menu
            bot.apply_menu(menu=time_frame_intervals_menu)

    elif message.text == 'Limit bars':
        max_bars = 10
        min_bars = 1
        __settings_to_change[1] = 'limit_bars'
        bot.send(text=f'Enter a bar\'s number (from {min_bars} to {max_bars})')

    elif message.text == 'Relative price change':
        max_value = 100
        min_value = 0.1
        __settings_to_change[1] = 'relative_price_change'
        bot.send(text=f'Enter a relative price change (from {min_value} to {max_value})')

    try:
        if __settings_to_change[1] == 'relative_price_change':
            value = float(message.text)
        else:
            value = int(message.text)
        __settings_to_change[0] = value
        save_settings(__settings_to_change)
        print(__settings_to_change[1], __settings_to_change[0])
        __settings_to_change = [0, '']
        bot.apply_menu(start_menu)
        bot.apply_menu(setting_menu)
    except ValueError:
        pass


bot.tbot.polling(non_stop=True)
