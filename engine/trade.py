from dataclasses import dataclass
import time

@dataclass
class Trade:
    buy_order_id: int
    sell_order_id: int
    stock: str
    price: float
    quantity: int
    timestamp: float = time.time()