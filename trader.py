import queue
import time
import threading
import random

from trader_sys import BollStrategy, MyRiskManager, Fill, Bitfinex, Application, MarketEvent


class Trader(Application):
    def __init__(self, strategy, portfolio, exchange, fill):
        self.strategy = strategy
        self.portfolio = portfolio
        self.exchange = exchange
        self.fill = fill
        threading.Thread(target=self._product_data).start()

    def _product_data(self):
        while True:
            rint = random.randint(0, 100)
            if rint > 50:
                self.events.put(MarketEvent(rint))
            time.sleep(10)

    def run_event_loop(self):
        while True:
            try:
                event = self.events.get(False)
            except queue.Empty:
                self.check_asset_status()
            else:
                if event.type == 'market':
                    self.strategy.run_strategy(event)
                elif event.type == 'signal':
                    self.portfolio.manage_risk(event)
                elif event.type == 'order':
                    self.exchange.execute_orders(event)
                elif event.type == 'fill':
                    self.fill.record_fill(event)

    def check_asset_status(self):
        # print('check position')
        position = self.exchange.fetch_position()
        # print(position)


if __name__ == '__main__':
    strategy = BollStrategy()
    risk_manager = MyRiskManager()
    exchange = Bitfinex()
    fill = Fill()
    trader = Trader(strategy, risk_manager, exchange, fill)
    trader.run_event_loop()
