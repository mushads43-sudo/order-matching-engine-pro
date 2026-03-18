from engine.order_book import OrderBook
from engine.trade import Trade
import threading

class MatchingEngine:
    def __init__(self, logger):
        self.order_book = OrderBook()
        self.trades = []
        self.lock = threading.Lock()
        self.logger = logger

    def add_order(self, order):
        with self.lock:
            self.order_book.add_order(order)
            self.match_orders(order.stock)

    def match_orders(self, stock):
        while True:
            best_buy = self.order_book.get_best_buy(stock)
            best_sell = self.order_book.get_best_sell(stock)

            if not best_buy or not best_sell:
                break

            if best_buy.price < best_sell.price:
                break

            trade_qty = min(best_buy.quantity, best_sell.quantity)
            trade_price = best_sell.price

            trade = Trade(
                buy_order_id=best_buy.order_id,
                sell_order_id=best_sell.order_id,
                stock=stock,
                price=trade_price,
                quantity=trade_qty
            )

            self.trades.append(trade)
            self.logger.log_trade(trade)

            best_buy.quantity -= trade_qty
            best_sell.quantity -= trade_qty

            if best_buy.quantity == 0:
                self.order_book.pop_best_buy(stock)

            if best_sell.quantity == 0:
                self.order_book.pop_best_sell(stock)