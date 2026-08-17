from typing import Any

from models.product import Product
from repositories.product_repository import ProductRepository


class InventoryService:
    def __init__(self) -> None:
        self.repository = ProductRepository()
        self.products = self.repository.load_products()

    def get_products(self) -> list[Product]:
        return self.products

    def get_product_by_sku(self, sku: str) -> Product | None:
        normalized_sku = sku.strip().upper()

        for product in self.products:
            if product.sku == normalized_sku:
                return product

        return None

    def add_product(
        self,
        sku: str,
        name: str,
        category: str,
        price: float,
        stock: int
    ) -> str:
        normalized_sku = sku.strip().upper()

        if self.get_product_by_sku(normalized_sku):
            return "SKU già presente"

        product = Product(
            normalized_sku,
            name,
            category,
            price,
            stock
        )

        self.products.append(product)
        self.repository.save_products(self.products)

        return "Prodotto aggiunto correttamente"

    def update_product(
        self,
        sku: str,
        new_value: Any,
        choice: int
    ) -> str:
        product = self.get_product_by_sku(sku)

        if product is None:
            return "Prodotto non trovato"

        if choice == 1:
            new_sku = str(new_value).strip().upper()

            existing_product = self.get_product_by_sku(new_sku)

            if existing_product is not None and existing_product is not product:
                return (
                    "Impossibile modificare: "
                    "SKU già associato ad un altro prodotto"
                )

            product.update_sku(new_sku)
            message = "SKU aggiornato correttamente"

        elif choice == 2:
            product.update_name(new_value)
            message = "Nome del prodotto aggiornato correttamente"

        elif choice == 3:
            product.update_category(new_value)
            message = "Categoria del prodotto aggiornata correttamente"

        elif choice == 4:
            product.update_price(new_value)
            message = "Prezzo del prodotto aggiornato correttamente"

        elif choice == 5:
            product.update_stock(new_value)
            message = "Quantità del prodotto aggiornata correttamente"

        else:
            return "Scelta non valida"

        self.repository.save_products(self.products)

        return message

    def delete_product(self, sku: str) -> str:
        product = self.get_product_by_sku(sku)

        if product is None:
            return "Prodotto non trovato"

        self.products.remove(product)

        self.repository.save_products(self.products)

        return "Prodotto eliminato correttamente"

    def reduce_stock(self, quantities: dict[str, int]) -> None:
        products_to_update = []

        for sku, quantity in quantities.items():
            if type(quantity) is not int or quantity <= 0:
                raise ValueError(
                    "La quantità deve essere un intero maggiore di zero."
                )

            product = self.get_product_by_sku(sku)

            if product is None:
                raise ValueError(f"Prodotto {sku} inesistente.")

            if quantity > product.stock:
                raise ValueError(
                    f"Stock insufficiente per {sku}. "
                    f"Disponibile: {product.stock}"
                )

            products_to_update.append((product, quantity))

        for product, quantity in products_to_update:
            product.update_stock(
                product.stock - quantity
            )

        self.repository.save_products(self.products)

    def restore_stock(self, quantities: dict[str, int]) -> None:
        products_to_update = []

        for sku, quantity in quantities.items():
            product = self.get_product_by_sku(sku)

            if product is None:
                raise ValueError(
                    f"Impossibile ripristinare lo stock: "
                    f"prodotto {sku} inesistente."
                )

            products_to_update.append((product, quantity))

        for product, quantity in products_to_update:
            product.update_stock(
                product.stock + quantity
            )

        self.repository.save_products(self.products)