from cli.product_menu import product_menu
from cli.order_menu import order_menu

def main_menu(inventory_service):
    while True:
        print('\n============= COMMERCECORE =============')
        print('1. Prodotti')
        print('2. Ordini')
        print('0. Esci')
        
        scelta = int(input('Scelta: '))
        
        if scelta == 0:
            break
        elif scelta == 1:
            product_menu(inventory_service)
        elif scelta == 2:
            order_menu(inventory_service)
        else:
            print('Scelta non valida')