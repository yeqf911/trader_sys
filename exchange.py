from abc import abstractmethod, ABC

import numpy as np
import pandas as pd

from trader_sys import Application
from trader_sys import FillEvent


# noinspection SpellCheckingInspection
class Exchange(ABC, Application):

    def execute_orders(self, event):
        print('------------------- new order -------------------')
        order = event.order

        if order == 1:
            self.buy('BTC', 4000, 1000)
        elif order == 0:
            self.sell('BTC', 4200, 1000)
        else:
            print('hold')
        print('------------------ order process finish ----------------\n')

    @abstractmethod
    def fetch_ohlcv(self, since=None, freq=None, limit=None):
        raise NotImplementedError('')

    @abstractmethod
    def fetch_position(self):
        raise NotImplementedError('')

    @abstractmethod
    def buy(self, symbol, price, quantity):
        raise NotImplementedError('')

    @abstractmethod
    def sell(self, symbol, price, quantity):
        raise NotImplementedError('')


class Bitfinex(Exchange):
    def fetch_ohlcv(self, since=None, freq=None, limit=None):
        data = np.random.standard_normal((20, 5))
        df = pd.DataFrame(data, columns=['open', 'high', 'low', 'close', 'volume'])
        return df

    def fetch_position(self):
        return np.random.rand(1000)

    def buy(self, symbol, price, quantity):
        buy_event = FillEvent(symbol, price, quantity, 'buy')
        self.events.put(buy_event)
        print('buy success symbol: {}\tprice: {}\tquantity: {}'.format(symbol, price, quantity))
        return 'success'

    def sell(self, symbol, price, quantity):
        sell_event = FillEvent(symbol, price, quantity, 'sell')
        self.events.put(sell_event)
        print('sell success symbol: {}\tprice: {}\tquantity: {}'.format(symbol, price, quantity))
        return 'success'
