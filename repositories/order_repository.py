import json
from json import JSONDecodeError


class OrderRepository:
    FILE_PATH = "data/orders.json"

    def load_orders(self) -> list[dict]:
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            return []

    def save_orders(self, orders: list[dict]) -> None:
        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(
                orders,
                file,
                indent=4,
                ensure_ascii=False
            )

    def add_order(self, order: dict) -> None:
        orders = self.load_orders()

        orders.append(order)

        self.save_orders(orders)