class OrderItem:
    def __init__(
        self,
        sku: str,
        name: str,
        quantity: int,
        unit_price: float
    ) -> None:
        if not isinstance(sku, str) or not sku.strip():
            raise ValueError("Lo SKU non può essere vuoto.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Il nome non può essere vuoto.")

        if type(quantity) is not int or quantity <= 0:
            raise ValueError(
                "La quantità deve essere un intero maggiore di zero."
            )

        if not isinstance(unit_price, (int, float)) or isinstance(
            unit_price,
            bool
        ):
            raise ValueError("Il prezzo deve essere un numero.")

        if unit_price <= 0:
            raise ValueError(
                "Il prezzo deve essere maggiore di zero."
            )

        self.sku = sku.strip().upper()
        self.name = name.strip()
        self.quantity = quantity
        self.unit_price = float(unit_price)

    def subtotal(self) -> float:
        return self.unit_price * self.quantity

    def to_dict(self) -> dict:
        return {
            "sku": self.sku,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.unit_price,
            "subtotal": self.subtotal()
        }