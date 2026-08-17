from models.order import Order
from models.order_item import OrderItem
from repositories.order_repository import OrderRepository
from services.inventory_service import InventoryService


class OrderService:
    def __init__(
        self,
        inventory_service: InventoryService
    ) -> None:
        self.inventory_service = inventory_service
        self.order_repository = OrderRepository()

    def create_order(
        self,
        requested_items: list[dict]
    ) -> Order:
        if not requested_items:
            raise ValueError(
                "L'ordine deve contenere almeno un prodotto."
            )

        quantities = {}

        # Raggruppa SKU duplicati
        for item in requested_items:
            sku = str(item["sku"]).strip().upper()
            quantity = item["quantity"]

            if type(quantity) is not int or quantity <= 0:
                raise ValueError(
                    f"Quantità non valida per {sku}."
                )

            quantities[sku] = (
                quantities.get(sku, 0)
                + quantity
            )

        order_items = []


        for sku, quantity in quantities.items():
            product = (
                self.inventory_service
                .get_product_by_sku(sku)
            )

            if product is None:
                raise ValueError(
                    f"Prodotto {sku} inesistente."
                )

            if quantity > product.stock:
                raise ValueError(
                    f"Stock insufficiente per {sku}. "
                    f"Disponibile: {product.stock}"
                )

            order_items.append(
                OrderItem(
                    sku=product.sku,
                    name=product.name,
                    quantity=quantity,
                    unit_price=product.price
                )
            )

        order = Order(
            self.generate_order_id(),
            order_items
        )

        self.inventory_service.reduce_stock(
            quantities
        )

        try:
            self.order_repository.add_order(
                order.to_dict()
            )
        except Exception:
            # rollback
            self.inventory_service.restore_stock(
                quantities
            )
            raise

        return order

    def get_orders(self) -> list[dict]:
        return self.order_repository.load_orders()

    def get_order_by_id(
        self,
        search_id: str
    ) -> dict | None:
        search_id = search_id.strip().upper()

        for order in self.order_repository.load_orders():
            if order["order_id"].upper() == search_id:
                return order

        return None

    def generate_order_id(self) -> str:
        highest_id = 0

        for order in self.order_repository.load_orders():
            try:
                number = int(
                    order["order_id"].split("-")[1]
                )

                highest_id = max(
                    highest_id,
                    number
                )

            except (
                KeyError,
                IndexError,
                ValueError
            ):
                continue

        return f"ORD-{highest_id + 1}"

    def cancel_order(
        self,
        cancel_id: str
    ) -> str:
        orders = self.order_repository.load_orders()

        cancel_id = cancel_id.strip().upper()

        order_to_cancel = None

        for order in orders:
            if order["order_id"].upper() == cancel_id:
                order_to_cancel = order
                break

        if order_to_cancel is None:
            return "Ordine inesistente."

        if order_to_cancel["status"] == "CANCELLED":
            return "L'ordine era già stato annullato."

        quantities = {}

        for item in order_to_cancel["products"]:
            sku = item["sku"]
            quantity = item["quantity"]

            quantities[sku] = (
                quantities.get(sku, 0)
                + quantity
            )

        self.inventory_service.restore_stock(
            quantities
        )

        order_to_cancel["status"] = "CANCELLED"

        try:
            self.order_repository.save_orders(
                orders
            )
        except Exception:
            # rollback
            self.inventory_service.reduce_stock(
                quantities
            )
            raise

        return "Ordine annullato con successo."