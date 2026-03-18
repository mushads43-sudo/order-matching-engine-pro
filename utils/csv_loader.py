import pandas as pd
from engine.order import Order

def load_orders_from_csv(path):
    df = pd.read_csv(path)
    orders = []

    for _, row in df.iterrows():
        order = Order(
            order_id=int(row["order_id"]),
            stock=row["stock"],
            side=row["side"],
            price=float(row["price"]),
            quantity=int(row["quantity"])
        )
        orders.append(order)

    return orders