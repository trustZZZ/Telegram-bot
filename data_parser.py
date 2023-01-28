import requests
import Time
from config import Configurator


class Coin:
    coins_names = Configurator.coins_names

    # "https://www.okx.cab/priapi/v5/market/candles?instId=MASK-USDT-SWAP&bar=15m&after=&limit=1000&t=1669496814127"
    @staticmethod
    def __get_json_file(coin_name, coin_pair, time_frame, limit_bars):
        if int(limit_bars) > 1000:
            limit_bars = 1000

        base_reference = "https://www.okx.cab/priapi/v5/market/candles?instId="
        reference = f"{base_reference}{coin_name}-{coin_pair}&bar={time_frame[0]}" \
                    f"{time_frame[1]}&after=&limit={limit_bars}"

        response = requests.get(reference)
        json_file = response.json()
        data = list(json_file['data'])
        return data

    @staticmethod
    def __generate_data_frame(data):
        import pandas as pd

        df = pd.DataFrame(columns=['Date', 'Open', 'Close', 'High', 'Low', 'relative_price', 'Volume'])

        for index in range(len(data[:])):
            df.loc[index, ['Date', 'Open', 'Close', 'High', 'Low', 'Volume']] = data[index][:6]
        df = df.astype('float')

        df['Date'] = pd.to_datetime(df['Date'], unit='ms')
        df['relative_price'] = ((df['Close'] - df['Open']) / df['Close'] * 100).round(2)

        return df

    @staticmethod
    def get_coin_data(time_frame=Time.minute(15), coin_name='DOGE', coin_pair='USDT', limit_bars=10):

        data = Coin.__get_json_file(time_frame=time_frame, coin_name=coin_name,
                                    coin_pair=coin_pair, limit_bars=limit_bars)
        df = Coin.__generate_data_frame(data)
        return df
