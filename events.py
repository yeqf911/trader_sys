class Event(object):
    pass
# hello world

class MarketEvent(Event):
    def __init__(self, bars):
        self.type = 'market'
        self.bars = bars


class SignalEvent(Event):
    def __init__(self, signal):
        self.type = 'signal'
        self.signal = signal


class OrderEvent(Event):
    def __init__(self, order):
        self.type = 'order'
        self.order = order


class FillEvent(Event):
    def __init__(self, symbol, price, quantity, action):
        self.type = 'fill'
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.action = action
