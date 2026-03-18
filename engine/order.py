from dataclasses import dataclass, field
import time

@dataclass(order=True)
class Order:
    sort_index: tuple = field(init=False, repr=False)
    order_id: int
    stock: str
    side: str  # BUY or SELL
    price: float
    quantity: int
    timestamp: float = field(default_factory=time.time)

    def __post_init__(self):
        if self.side == "BUY":
            self.sort_index = (-self.price, self.timestamp)
        else:
            self.sort_index = (self.price, self.timestamp)