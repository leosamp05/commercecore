from cli.main_menu import main_menu
from services.inventory_service import InventoryService

inventory_service = InventoryService()

main_menu(inventory_service)