from models.product import Product

class InventoryService:
    def __init__(self):
        self.products = []
    
    def add_product(self, sku, name, category, price, stock):
        for product in self.products:
            if sku == product.sku:
                return 'SKU già presente'
        
        new_product = Product(sku, name, category, price, stock)
        self.products.append(new_product)
    
    def get_products(self):
        return self.products
        