from engine.matching_engine import MatchingEngine
from utils.logger import TradeLogger
from utils.csv_loader import load_orders_from_csv

def main():
    logger = TradeLogger()
    engine = MatchingEngine(logger)

    orders = load_orders_from_csv("data/orders.csv")

    for order in orders:
        engine.add_order(order)

    print("\n✅ Trades Executed:\n")
    for trade in engine.trades:
        print(
            f"{trade.stock} | Price: {trade.price} | Qty: {trade.quantity} | BuyID: {trade.buy_order_id} | SellID: {trade.sell_order_id}"
        )

if __name__ == "__main__":
    main()