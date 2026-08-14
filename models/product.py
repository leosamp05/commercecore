class Product:
    def __init__(self, sku: str, name: str, category: str, price: float, stock: int) -> None:
        if not sku.strip():
            raise ValueError("SKU cannot be empty.")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if not category.strip():
            raise ValueError("Category cannot be empty.")

        if not isinstance(price, (int, float)) or isinstance(price, bool):
            raise ValueError("Price must be a number.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        if type(stock) is not int:
            raise ValueError("Stock must be an integer.")

        if stock < 0:
            raise ValueError("Stock cannot be negative.")
        
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        
    def __str__(self) -> str:
        return f"{self.sku} - {self.name} - €{self.price:.2f} - Stock: {self.stock}"
    
    