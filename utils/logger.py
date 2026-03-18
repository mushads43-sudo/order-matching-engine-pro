import logging

class TradeLogger:
    def __init__(self):
        logging.basicConfig(
            filename="logs/trades.log",
            level=logging.INFO,
            format="%(asctime)s - %(message)s"
        )

    def log_trade(self, trade):
        logging.info(
            f"TRADE | Stock: {trade.stock} | Price: {trade.price} | Qty: {trade.quantity} | BuyID: {trade.buy_order_id} | SellID: {trade.sell_order_id}"
        )