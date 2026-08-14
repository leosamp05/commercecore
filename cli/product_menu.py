def product_menu(inventory_service):
    while True:
        print('\n========PRODOTTI========')
        print('1. Visualizza Prodotti')
        print('2. Aggiungi un Prodotto')
        print('0. Indietro')
        
        try:
            scelta = int(input('Scelta: '))
        except ValueError as error:
            print(f"Errore: {error}")
            continue
        
        if scelta == 0:
            break
        
        elif scelta == 1:
            products = inventory_service.get_products()
            
            separator = '-' * 75
            
            print(separator)
            print(f"{'SKU':<22}{'NAME':<30}{'PREZZO':<13}{'STOCK':<8}")
            print(separator)
            
            for product in products:
                print(
                    f"{product.sku:<22}"
                    f"{product.name:<30}"
                    f"€{product.price:<12.2f}"
                    f"{product.stock:<8}"       
                )
            
            
        elif scelta == 2:
            try:
                sku = input('SKU: ')
                name = input('Nome: ')
                category = input('Categoria: ')
                price = float(input('Prezzo: '))
                stock = int(input('Stock: '))
                
                result = inventory_service.add_product(sku, name, category, price, stock)
            except ValueError as error:
                print(f"Errore: {error}")
        
        else:
            print('Scelta non valida\n')
    