import heapq
from collections import defaultdict

class OrderBook:
    def __init__(self):
        self.buy_orders = defaultdict(list)   # max heap
        self.sell_orders = defaultdict(list)  # min heap

    def add_order(self, order):
        if order.side == "BUY":
            heapq.heappush(self.buy_orders[order.stock], order)
        else:
            heapq.heappush(self.sell_orders[order.stock], order)

    def get_best_buy(self, stock):
        return self.buy_orders[stock][0] if self.buy_orders[stock] else None

    def get_best_sell(self, stock):
        return self.sell_orders[stock][0] if self.sell_orders[stock] else None

    def pop_best_buy(self, stock):
        return heapq.heappop(self.buy_orders[stock])

    def pop_best_sell(self, stock):
        return heapq.heappop(self.sell_orders[stock])