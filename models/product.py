class Product:
    def __init__(
        self,
        sku: str,
        name: str,
        category: str,
        price: float,
        stock: int
    ) -> None:
        self.update_sku(sku)
        self.update_name(name)
        self.update_category(category)
        self.update_price(price)
        self.update_stock(stock)

    def update_sku(self, new_sku: str) -> None:
        if not isinstance(new_sku, str) or not new_sku.strip():
            raise ValueError("Lo SKU non può essere vuoto.")

        self.sku = new_sku.strip().upper()

    def update_name(self, new_name: str) -> None:
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError("Il nome non può essere vuoto.")

        self.name = new_name.strip()

    def update_category(self, new_category: str) -> None:
        if not isinstance(new_category, str) or not new_category.strip():
            raise ValueError("La categoria non può essere vuota.")

        self.category = new_category.strip()

    def update_price(self, new_price: float) -> None:
        if not isinstance(new_price, (int, float)) or isinstance(new_price, bool):
            raise ValueError("Il prezzo deve essere un numero.")

        if new_price <= 0:
            raise ValueError("Il prezzo deve essere maggiore di zero.")

        self.price = float(new_price)

    def update_stock(self, new_stock: int) -> None:
        if type(new_stock) is not int:
            raise ValueError("Lo stock deve essere un numero intero.")

        if new_stock < 0:
            raise ValueError("Lo stock non può essere negativo.")

        self.stock = new_stock

    def __str__(self) -> str:
        return (
            f"{self.sku} - {self.name} - "
            f"€{self.price:.2f} - Stock: {self.stock}"
        )