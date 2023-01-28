import datetime
from data_parser import Coin
import bot


class MonitoringBot:

    def __init__(self):
        bot.send(text="BOT HAS BEEN INITIALIZED")

    @staticmethod
    def stop():
        bot.monitoring = False

    @staticmethod
    def start():
        from graph import CandleStick
        bot.monitoring = True
        coins_names = bot.settings.coins_names
        time_frame = bot.settings.time_frame
        limit_bars = bot.settings.limit_bars
        chat_id = bot.settings.chat_id
        bot.send(text=r"Monitoring has been started", chat_id=chat_id)

        while bot.monitoring:
            try:
                for coin_name in {k: v for (k, v) in coins_names.items() if v <= datetime.datetime.now()}.keys():
                    if not bot.monitoring:
                        break
                    df = Coin.get_coin_data(time_frame=time_frame, coin_name=coin_name, limit_bars=limit_bars)
                    if df.loc[0, 'relative_price'] > bot.settings.relative_price_change:
                        coins_names[coin_name] += datetime.timedelta(minutes=5)
                        CandleStick.draw_chart(df=df, coin_name=coin_name)
            except Exception as e:
                bot.send(text=f'Unexpected error: {e}',
                              chat_id=chat_id)
        bot.send(text='Monitoring has been stopped', chat_id=chat_id)
