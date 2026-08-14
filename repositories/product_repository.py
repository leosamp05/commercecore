import json
from models.product import Product


class ProductRepository:
    def load_products(self) -> list:
        with open("data/products.json", "r") as file:
            data = json.load(file)

        products = []

        for item in data:
            product = Product(
                item["sku"],
                item["name"],
                item["category"],
                item["price"],
                item["stock"]
            )

            products.append(product)

        return products           
            
    def save_products(self, products) -> None:
        data = []
        for product in products:
            item = {
                "sku": product.sku,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "stock": product.stock
            }
            
            data.append(item)
            
        with open("data/products.json", "w") as file:
            json.dump(data, file, indent=4)
            
        