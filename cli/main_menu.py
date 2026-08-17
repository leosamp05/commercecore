from cli.order_menu import order_menu
from cli.product_menu import product_menu


def main_menu(inventory_service) -> None:
    while True:
        print("\n============= COMMERCECORE =============")
        print("1. Prodotti")
        print("2. Ordini")
        print("0. Esci")

        try:
            scelta = int(input("Scelta: "))
        except ValueError:
            print("Scelta non valida")
            continue

        if scelta == 0:
            break

        elif scelta == 1:
            product_menu(inventory_service)

        elif scelta == 2:
            order_menu(inventory_service)

        else:
            print("Scelta non valida")