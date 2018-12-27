from abc import abstractmethod, ABC
import random
from trader_sys import Application
from trader_sys import SignalEvent, OrderEvent


class RiskManager(ABC, Application):
    def manage_risk(self, event):
        if not isinstance(event, SignalEvent):
            return
        order = self.handle_signal(event.signal)
        order_event = OrderEvent(order)
        self.events.put(order_event)

    @abstractmethod
    def handle_signal(self, signal):
        raise NotImplementedError('should be implement')


class MyRiskManager(RiskManager):
    def handle_signal(self, signal):
        print('manager risk finish')
        if signal == 1:
            return random.randint(0, 1)
