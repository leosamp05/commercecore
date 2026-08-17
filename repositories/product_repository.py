import json
from json import JSONDecodeError

from models.product import Product


class ProductRepository:
    FILE_PATH = "data/products.json"

    def load_products(self) -> list[Product]:
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            return []

        products = []

        for item in data:
            products.append(
                Product(
                    item["sku"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["stock"]
                )
            )

        return products

    def save_products(self, products: list[Product]) -> None:
        data = []

        for product in products:
            data.append({
                "sku": product.sku,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "stock": product.stock
            })

        with open(self.FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )