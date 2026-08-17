from datetime import datetime

from models.order_item import OrderItem


class Order:
    def __init__(
        self,
        order_id: str,
        items: list[OrderItem]
    ) -> None:
        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError(
                "L'ID ordine non può essere vuoto."
            )

        if not items:
            raise ValueError(
                "L'ordine deve contenere almeno un prodotto."
            )

        self.order_id = order_id
        self.items = items
        self.created_at = datetime.now()
        self.status = "CONFIRMED"

    def total(self) -> float:
        return sum(
            item.subtotal()
            for item in self.items
        )

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "created": self.created_at.isoformat(),
            "status": self.status,
            "products": [
                item.to_dict()
                for item in self.items
            ],
            "total": self.total()
        }