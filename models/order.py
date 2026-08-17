from datetime import datetime

class Order:
    def __init__(self, order_id: str, items: list) -> None:
        
        if not items:
            raise ValueError("Order must contain at least one item.")

        self.order_id = order_id
        self.items = items
        self.created_at = datetime.now()
        self.status = 'CONFIRMED'

    def total(self):
        return sum(item.subtotal() for item in self.items)
        
        
        