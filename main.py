from cli.main_menu import main_menu
from services.inventory_service import InventoryService


def main() -> None:
    inventory_service = InventoryService()

    main_menu(
        inventory_service
    )


if __name__ == "__main__":
    main()