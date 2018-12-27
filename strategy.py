import time
from abc import abstractmethod, ABC
import random
from trader_sys import Application
from trader_sys import MarketEvent, SignalEvent


class Strategy(ABC, Application):
    def run_strategy(self, event):
        if not isinstance(event, MarketEvent):
            return
        signal = self.handler_bars(bars=event.bars)
        self.events.put(SignalEvent(signal))

    @abstractmethod
    def handler_bars(self, bars):
        raise NotImplementedError('should be implement')


class BollStrategy(Strategy):
    def handler_bars(self, bars):
        time.sleep(1)
        print('process signal {}'.format(str(bars)))
        return random.randint(0, 1)
