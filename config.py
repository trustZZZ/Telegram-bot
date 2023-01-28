import datetime
import Time


class Configurator:
    __token = ''
    __chat_id = ''
    __time_frame = Time.minute(15)
    __limit_bars = 10
    __relative_price_change = 1.0
    __path_to_save = r'Coins_charts'
    __coins_names = ["LTC", "AGLD", "DOGE",
                     "SLP", "RSR", "UMEE",
                     "IOST", "SWEAT", "USTC",
                     "JST", "ZIL", "PEOPLE",
                     "GALA", "CFX", "CSPR",
                     "DOME", "FITFI", "GRT",
                     "CRO", "REN", "FLM",
                     "ALPHA", "XLM", "CVC"]

    @property
    def token(self) -> str:
        return str(self.__token)

    @token.setter
    def token(self, token: str) -> None:
        if token and type(token) == str:
            self.__token = token

    @property
    def chat_id(self) -> str:
        return self.__chat_id

    @chat_id.setter
    def chat_id(self, chat_id) -> None:
        if chat_id and type(chat_id) == str:
            self.__chat_id = chat_id

    @property
    def time_frame(self) -> tuple:
        return self.__time_frame

    @time_frame.setter
    def time_frame(self, time_frame: tuple) -> None:
        if time_frame and type(time_frame) == tuple:
            self.__time_frame = time_frame

    @property
    def limit_bars(self) -> int:
        return self.__limit_bars

    @limit_bars.setter
    def limit_bars(self, limit_bars: int) -> None:
        if limit_bars and type(limit_bars) == int and limit_bars > 0:
            self.__limit_bars = limit_bars

    @property
    def relative_price_change(self) -> float:
        return float(self.__relative_price_change)

    @relative_price_change.setter
    def relative_price_change(self, relative_price_change: float) -> None:
        if relative_price_change and type(relative_price_change) == float:
            self.__relative_price_change = relative_price_change

    @property
    def coins_names(self) -> dict:
        coins_list = {}
        for coin in self.__coins_names:
            coins_list[coin] = datetime.datetime.now()
        return coins_list

    @coins_names.setter
    def coins_names(self, coins_list: list) -> None:
        if coins_list and type(coins_list) == list:
            self.__coins_names = coins_list

    @property
    def path_to_save(self):
        return self.__path_to_save

    @path_to_save.setter
    def path_to_save(self, path_to_save):
        import os
        if os.path.exists(path_to_save):
            self.__path_to_save = path_to_save

    def set_configurations(self, token: str = None, chat_id: str = None, limit_bars: int = None,
                           time_frame: tuple = None,
                           relative_price_change: float = None, coins_list: list = None,
                           path_to_save: str = None) -> None:
        if token:
            self.__token = token
        if chat_id:
            self.__chat_id = chat_id
        if limit_bars:
            self.__limit_bars = limit_bars if (limit_bars <= 10) & (limit_bars > 0) else 10
        if time_frame:
            self.__time_frame = time_frame
        if relative_price_change:
            self.__relative_price_change = relative_price_change if (relative_price_change <= 100) & (
                        relative_price_change >= 0.1) else 1.0
        if coins_list:
            self.__coins_names = coins_list
        if path_to_save:
            self.__path_to_save = path_to_save
