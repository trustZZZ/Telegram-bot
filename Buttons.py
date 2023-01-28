from telebot import types


class Buttons(object):

    start_monitoring = types.InlineKeyboardButton(text="Start monitoring", callback_data='START')
    stop_monitoring = types.InlineKeyboardButton(text="Stop monitoring", callback_data='STOP')
    settings = types.InlineKeyboardButton(text="Settings", callback_data='OPEN_SETTINGS')

    back = types.KeyboardButton(text='Back')

    time_frame = types.KeyboardButton(text="Time frame")
    limit_bars = types.KeyboardButton(text='Limit bars')
    relative_price_change = types.KeyboardButton(text='Relative price change')

    @staticmethod
    def set_buttons(values: list) -> list:
        buttons = []
        for value in values:
            buttons.append(types.KeyboardButton(text=f'{str(value)}'))
        return buttons
