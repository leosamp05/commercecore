from models.product import Product
from services.inventory_service import InventoryService

class OrderItem:
    def __init__(self, product: dict) -> None:
        self.product = product
        
    def subtotal(self) -> float:
        inventory_service = InventoryService()
        products = inventory_service.get_products()
        
        for product in products:
            if self.product['sku'] == product.sku:
                unit_price = product.price
        
        quantity = self.product['quantity']
              
        return unit_price * quantity