from abc import ABC

from trader_sys import Application


class Fill(ABC, Application):
    def record_fill(self, event):
        print('========RECORD action: {}\tsymbol: {}\tquantity: {}\tprice: {}\n'.format(event.action, event.symbol,
                                                                                        event.quantity,
                                                                                        event.price))
