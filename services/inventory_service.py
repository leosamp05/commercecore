from models.product import Product
from repositories.product_repository import ProductRepository


class InventoryService:
    def __init__(self) -> None:
        self.repository = ProductRepository()
        self.products = self.repository.load_products()
    
    def add_product(self, sku: str, name: str, category: str, price: float, stock: int) -> str | None:
        for product in self.products:
            if sku == product.sku:
                return "SKU già presente"

        new_product = Product(
            sku,
            name,
            category,
            price,
            stock
        )

        self.products.append(new_product)

        self.repository.save_products(self.products)
    
    def get_products(self) -> list:
        return self.products
    
    def update_product(self, sku: str, new_value: str | float | int, choice: int) -> str:
        if choice == 1:
            for product in self.products:
                if new_value == product.sku:
                    return 'Impossibile modificare: SKU già associato ad un altro prodotto'
            
            for product in self.products:
                if sku == product.sku:
                    product.update_sku(new_value)
                    self.repository.save_products(self.products)
                    return 'SKU aggiornato correttamente'    
        elif choice == 2:
            for product in self.products:
                if sku == product.sku:
                    product.update_name(new_value)
                    self.repository.save_products(self.products)
                    return 'Nome del prodotto aggiornato correttamente'
        elif choice == 3:
            for product in self.products:
                if sku == product.sku:
                    product.update_category(new_value)
                    self.repository.save_products(self.products)
                    return 'Categoria del prodotto aggiornata correttamente'
        elif choice == 4:
            for product in self.products:
                if sku == product.sku:
                    product.update_price(new_value)
                    self.repository.save_products(self.products)
                    return 'Prezzo del prodotto aggiornato correttamente'
        elif choice == 5:
            for product in self.products:
                if sku == product.sku:
                    product.update_stock(new_value)
                    self.repository.save_products(self.products)
                    return 'Quantità del prodotto aggiornata correttamente'
        
    def delete_product(self, sku: str) -> None:
        if not sku.strip():
            raise ValueError("Lo sku non può essere vuoto.")
                
        for index, product in enumerate(self.products):
            if sku == product.sku:
                self.products.pop(index)
                self.repository.save_products(self.products)
                return 'Prodotto eliminato correttamente'
                
        return 'Prodotto non trovato'
        