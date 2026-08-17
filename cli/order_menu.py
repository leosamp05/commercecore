from services.order_service import OrderService

def order_menu(inventory_service) -> str:
    order_service = OrderService()
    
    while True:
        print('\n============= ORDINI =============')
        print('1. Nuovo ordine')
        print('2. Visualizza ordini')
        print('3. Dettaglio ordine')
        print('4. Annulla ordine')
        print('0. Indietro')
        
        try:
            scelta = int(input('\nScelta: '))
        except ValueError as error:
            print(f"Errore: {error}")
            continue
        
        if scelta == 1:
            products = inventory_service.get_products()
            proceed = 's'
            order = []
            
            
            print('\n============= NUOVO ORDINE =============')
            while proceed == 's':
                try:
                    sku = input('\nSKU prodotto: ')
                    quantity = int(input('Quantità: '))
                except ValueError as error:
                    print(f"Errore: {error}")
                    continue
                
                if not sku.strip():
                    raise ValueError('Lo SKU non deve essere vuoto.')
                
                if type(quantity) is not int:
                    raise ValueError('La quantità deve essere un numero intero')
                
                if quantity <= 0:
                    print('Inserire una quantità valida.')
                    continue
                
                exists = False
                for product in products:
                    if sku == product.sku:
                        exists = True
                        if quantity <= product.stock:
                            order.append({
                                'sku': sku, 
                                'quantity': quantity,
                                'price': product.price
                            })
                        
                            print('Prodotto aggiunto:') 
                            print(f'{sku} - {product.name} x{quantity}')
                        else:
                            print('Prodotto non disponibile nella quantità richiesta.\n')

                if not exists:
                    print('Prodotto inesistente.')
                
                while True:        
                    proceed = input('Aggiungere un altro prodotto? [s/n]: ')
                    if str(proceed.strip().lower()) == 's' or str(proceed.strip().lower()) == 'n':
                        break
                    
                if proceed == 'n':
                    break
                
            total = 0
            print('\n============= RIEPILOGO =============\n')
            for dic in order:
                for product in products:
                    if dic['sku'] == product.sku:
                        total += product.price * dic['quantity']
                        print(f"{product.sku} - {product.name :<15} - x{dic['quantity']} - {product.price * dic['quantity']}")

            print(f'\nTotale: {total}')
                        
                        
            while True:        
                proceed = input('Confermare ordine? [s/n]: ')
                if str(proceed.strip().lower()) == 's' or str(proceed.strip().lower()) == 'n':
                    break
            
            if proceed == 'n':
                print('Ordine annullato')
                break
            
            if proceed == 's':
                order_service.create_order(order)
                print('Ordine confermato.')
                break
                    
            
        elif scelta == 2:
            print(order_service.get_orders())
        elif scelta == 3:
            try:
                order_id = input('Inserire ID Ordine: ')
            except ValueError as error:
                print(f"Errore: {error}")
                continue
            
            if not order_id.strip():
                raise ValueError("L'ID Ordine non deve essere vuoto.")
            
            order_service.get_order_by_id(order_id)
            
        elif scelta == 4:
            cancel_id = input("Inserire l'ID dell'ordine da annullare: ")
            
            if not  cancel_id.strip():
                raise ValueError("L'ID Ordine non deve essere vuoto.")
            
            order_service.cancel_order(cancel_id)
            
        elif scelta == 0:
            break
        else:
            print('Scelta non valida\n')