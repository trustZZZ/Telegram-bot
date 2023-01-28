import pandas as pd
import mplfinance as mpf
import bot


class CandleStick(object):

    @staticmethod
    def __get_image_path(image_folder: str = bot.settings.path_to_save):
        import os
        import datetime

        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        image_path = "\\".join([image_folder, (str(datetime.datetime.now().time().strftime("%H_%M")) + ".png")])
        return image_path

    @staticmethod
    def draw_chart(df=pd.DataFrame(data=[], columns=[]), coin_name='COIN'):
        saved_image = CandleStick.__get_image_path()

        ###########################################################################
        open_price = df.loc[0, 'Open']
        close_price = df.loc[0, 'Close']
        relative_price = df.loc[0, 'relative_price']
        ###########################################################################

        candles = pd.DataFrame(columns=['Date', 'Open', 'Close', 'High', 'Low', 'Volume'],
                               data=df.loc[:, ['Date', 'Open', 'Close', 'High', 'Low', 'Volume']])
        candles.set_index("Date", inplace=True)
        candles = candles.iloc[::-1].tail(10)
        candles.index.name = 'Date'

        title = str(f"Open:{open_price} Close:{close_price} || {relative_price}%")

        mpf.plot(data=candles, type='candle', volume=True,
                 savefig=saved_image, style='yahoo', title=title)
        bot.send(text=f'CHANGING: {coin_name}', photo_path=saved_image)
