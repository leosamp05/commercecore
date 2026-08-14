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
    
    def update_sku(self, new_sku: str) -> None:
        if not new_sku.strip():
            raise ValueError("Lo sku non può essere vuoto.")

        self.sku = new_sku
        
    def update_name(self, new_name: str) -> None:
        if not new_name.strip():
            raise ValueError("Il nome non può essere vuoto.")

        self.name = new_name
        
    def update_category(self, new_category: str) -> None:
        if not new_category.strip():
            raise ValueError("La categoria non può essere vuota.")

        self.name = new_category
        
    def update_name(self, new_price: str) -> None:
        if not new_price.strip():
            raise ValueError("Il prezzo non può essere vuoto.")
        
        if not isinstance(new_price, (int, float)) or isinstance(new_price, bool):
            raise ValueError("Il prezzo deve essere un numero.")

        if new_price <= 0:
            raise ValueError("Il prezzo deve essere maggiore di zero.")

        self.price = new_price
        
    def update_stock(self, new_stock: int) -> None:
        if type(new_stock) is not int:
            raise ValueError("Lo stock deve essere un numero intero.")

        if new_stock < 0:
            raise ValueError("Lo stock non può essere negativo.")

        self.stock = new_stock
        
    def __str__(self) -> str:
        return f"{self.sku} - {self.name} - €{self.price:.2f} - Stock: {self.stock}"
    
    