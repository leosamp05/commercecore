from services.order_service import OrderService


def print_order(order: dict) -> None:
    print(f"\n{order['order_id']}")
    print(f"Data: {order['created']}")
    print(f"Stato: {order['status']}")

    for item in order["products"]:
        name = item.get(
            "name",
            "Nome non disponibile"
        )

        subtotal = item.get(
            "subtotal",
            item["price"] * item["quantity"]
        )

        print(
            f"{item['sku']} - "
            f"{name} - "
            f"x{item['quantity']} - "
            f"€{subtotal:.2f}"
        )

    print(
        f"Totale: €{order['total']:.2f}"
    )


def order_menu(inventory_service) -> None:
    order_service = OrderService(
        inventory_service
    )

    while True:
        print("\n============= ORDINI =============")
        print("1. Nuovo ordine")
        print("2. Visualizza ordini")
        print("3. Dettaglio ordine")
        print("4. Annulla ordine")
        print("0. Indietro")

        try:
            scelta = int(input("\nScelta: "))
        except ValueError:
            print("Scelta non valida")
            continue

        if scelta == 0:
            break

        elif scelta == 1:
            requested_items = []

            print(
                "\n============= NUOVO ORDINE ============="
            )

            while True:
                sku = input(
                    "\nSKU prodotto: "
                ).strip().upper()

                if not sku:
                    print(
                        "Lo SKU non può essere vuoto."
                    )
                    continue

                product = (
                    inventory_service
                    .get_product_by_sku(sku)
                )

                if product is None:
                    print("Prodotto inesistente.")
                    continue

                try:
                    quantity = int(
                        input("Quantità: ")
                    )
                except ValueError:
                    print(
                        "La quantità deve essere "
                        "un numero intero."
                    )
                    continue

                if quantity <= 0:
                    print(
                        "Inserire una quantità valida."
                    )
                    continue

                already_requested = sum(
                    item["quantity"]
                    for item in requested_items
                    if item["sku"] == sku
                )

                if (
                    already_requested + quantity
                    > product.stock
                ):
                    print(
                        "Prodotto non disponibile "
                        "nella quantità richiesta. "
                        f"Disponibile: {product.stock}"
                    )
                    continue

                requested_items.append({
                    "sku": sku,
                    "quantity": quantity
                })

                print(
                    f"Prodotto aggiunto: "
                    f"{product.sku} - "
                    f"{product.name} x{quantity}"
                )

                while True:
                    proceed = input(
                        "Aggiungere un altro "
                        "prodotto? [s/n]: "
                    ).strip().lower()

                    if proceed in ("s", "n"):
                        break

                    print(
                        "Inserisci 's' oppure 'n'."
                    )

                if proceed == "n":
                    break

            if not requested_items:
                print(
                    "Nessun prodotto aggiunto."
                )
                continue

            print(
                "\n============= RIEPILOGO ============="
            )

            total = 0.0

            for item in requested_items:
                product = (
                    inventory_service
                    .get_product_by_sku(
                        item["sku"]
                    )
                )

                subtotal = (
                    product.price
                    * item["quantity"]
                )

                total += subtotal

                print(
                    f"{product.sku} - "
                    f"{product.name} - "
                    f"x{item['quantity']} - "
                    f"€{subtotal:.2f}"
                )

            print(
                f"\nTotale: €{total:.2f}"
            )

            while True:
                proceed = input(
                    "Confermare ordine? [s/n]: "
                ).strip().lower()

                if proceed in ("s", "n"):
                    break

                print(
                    "Inserisci 's' oppure 'n'."
                )

            if proceed == "n":
                print("Ordine annullato.")
                continue

            try:
                order = order_service.create_order(
                    requested_items
                )

                print(
                    "Ordine confermato. "
                    f"ID ordine: {order.order_id}"
                )

            except ValueError as error:
                print(f"Errore: {error}")

        elif scelta == 2:
            orders = order_service.get_orders()

            if not orders:
                print("Nessun ordine presente.")
                continue

            print(
                f"\nStorico Ordini ({len(orders)}):"
            )

            for order in orders:
                print_order(order)

        elif scelta == 3:
            order_id = input(
                "Inserire ID Ordine: "
            ).strip()

            if not order_id:
                print(
                    "L'ID ordine non può essere vuoto."
                )
                continue

            order = order_service.get_order_by_id(
                order_id
            )

            if order is None:
                print("Ordine inesistente.")
            else:
                print_order(order)

        elif scelta == 4:
            cancel_id = input(
                "Inserire l'ID dell'ordine "
                "da annullare: "
            ).strip()

            if not cancel_id:
                print(
                    "L'ID ordine non può essere vuoto."
                )
                continue

            try:
                print(
                    order_service.cancel_order(
                        cancel_id
                    )
                )
            except ValueError as error:
                print(f"Errore: {error}")

        else:
            print("Scelta non valida")