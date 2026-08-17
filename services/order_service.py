from models.order_item import OrderItem
from models.order import Order
from repositories.order_repository import OrderRepository
from services.inventory_service import InventoryService

class OrderService:
    def  __init__(self):
        self.inventory_service = InventoryService()
        self.order_repository = OrderRepository()
        
        
    def create_order(self, order):
        order_items = []
        for product in order:
            order_items.append(
                OrderItem(product)
            )
            
        ordine = Order(self.generate_order_id(), order_items)
        
        self.order_repository.save_order({
            'order_id': ordine.order_id,
            'created': ordine.created_at.isoformat(),
            'status': ordine.status,
            'products': order,
            'total': ordine.total(),
        })
        
        for product in order:
            for prodotto in self.inventory_service.get_products():
                if product['sku'] == prodotto.sku:
                    stock = prodotto.stock
            self.inventory_service.update_product(product['sku'], (stock - product['quantity']), 5)

        print(f'\n\nID ORDINE: {ordine.order_id}')
    
    def get_orders(self):
        orders = self.order_repository.load_orders()
        
        print(f'\nStorico Ordini {len(orders)}:')
        for order in orders:
            print('\n' + order['order_id'])
            print(order['created'])
            print(order['status'])
            for product in order['products']:
                for prodotto in self.inventory_service.get_products():
                    if product['sku'] == prodotto.sku:
                        total = product['price'] * product['quantity']
                        print(f'{product['sku']} - {prodotto.name} - x{product['quantity']} - {total}')
                        
            print(f'Totale: {order['total']}')
            print('\n')
            
    
    def get_order_by_id(self, search_id: str):
        orders = self.order_repository.load_orders()
        
        exists = False
        print(f'\nOrdine {search_id}:')
        for order in orders:
            if order['order_id'] == search_id:
                exists = True
                print('\n' + order['order_id'])
                print(order['created'])
                print(order['status'])
                for product in order['products']:
                    for prodotto in self.inventory_service.get_products():
                        if product['sku'] == prodotto.sku:
                            total = product['price'] * product['quantity']
                            print(f'{product['sku']} - {prodotto.name} - x{product['quantity']} - {total}')
                        
                print(f'Totale: {order['total']}')
                print('\n')

        if not exists:
            print('Ordine inesistente.')
    
    def generate_order_id(self):
        orders = self.order_repository.load_orders()
        
        if not orders:
            new_id = 0
        else:
            new_id = int(orders[len(orders) - 1]['order_id'][4:]) + 1
        
        new_order_id = 'ORD-' + str(new_id)
        
        return new_order_id
    
    def cancel_order(self, cancel_id):
        orders = self.order_repository.load_orders()

        exists = False
        for index, order in enumerate(orders):
            if cancel_id == order['order_id']:
                exists = True
                self.order_repository.cancel_order(index)
                
                
        if not exists:
            print('Ordine inesistente.')
            

            
            
            
        

        