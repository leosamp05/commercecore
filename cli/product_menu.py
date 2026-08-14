def product_menu(inventory_service) -> str:
    while True:
        print('\n========PRODOTTI========')
        print('1. Visualizza Prodotti')
        print('2. Aggiungi un Prodotto')
        print('3. Modifica un Prodotto')
        print('4. Elimina un Prodotto')
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
            
            separator = '-' * 100
            
            print('\n', separator)
            print(f"{'SKU':<22}{'NOME':<30}{'CATEGORIA':<25}{'PREZZO':<13}{'STOCK':<8}")
            print(separator)
            
            if not products:
                print('Lista vuota'.center(75))
            else:
                for product in products:
                    print(
                        f"{product.sku:<22}"
                        f"{product.name:<30}"
                        f"{product.category:<25}",
                        f"€{product.price:<12.2f}"
                        f"{product.stock:<8}"       
                    )
                
            print(separator)

        elif scelta == 2:
            try:
                sku = input('SKU: ')
                name = input('Nome: ')
                category = input('Categoria: ')
                price = float(input('Prezzo: '))
                stock = int(input('Stock: '))
                
                inventory_service.add_product(sku, name, category, price, stock)
            except ValueError as error:
                print(f"Errore: {error}")
                
        elif scelta == 3:
            sku = input('SKU: ')
            sku = sku.upper()
            
            products = inventory_service.get_products()
            
            exists = False
            for product in products:
                if sku == product.sku:
                    exists = True
                    
            if not exists:
                print(f'{sku} non esistente')
                continue
            
            while True:
                print('\nScegli il campo da aggiornare:')
                print('1. SKU')
                print('2. Nome')
                print('3. Categoria')
                print('4. Prezzo')
                print('5. Stock')
                print('0. Indietro')
                
                try:
                    update = int(input("Scelta: "))
                except ValueError:
                    print("Scelta non valida")
                    continue
                print('\n')
                
                if update == 1:
                    new_value = input('Nuovo SKU: ')
                    new_value = new_value.upper()
                elif update == 2:
                    new_value = input('Nuovo Nome: ')
                elif update == 3:
                    new_value = input('Nuova Categoria: ')
                elif update == 4:
                    new_value = float(input('Nuovo Prezzo: '))
                elif update == 5:
                    new_value = int(input('Nuovo Stock: '))
                elif update == 0:
                    break
                else:
                    print('Scelta non valida\n')
                    continue
                
                print(inventory_service.update_product(sku, new_value, update))
                if update == 1:
                    break

        elif scelta == 4:
            sku = input('SKU da eliminare: ')
            print(inventory_service.delete_product(sku))
        
        else:
            print('Scelta non valida\n')
    