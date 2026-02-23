import logging


logger = logging.getLogger(__name__)


VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT", "STOP_LIMIT"}


def validate_symbol(symbol: str) -> str:
    if not symbol or not symbol.strip():
        raise ValueError("Symbol cannot be empty.")

    return symbol.upper()


def validate_side(side: str) -> str:
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side. Allowed values: {VALID_SIDES}")

    return side


def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type. Allowed values: {VALID_ORDER_TYPES}"
        )

    return order_type


def validate_quantity(quantity) -> float:
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price, order_type: str):
    if order_type in {"LIMIT", "STOP_LIMIT"}:
        if price is None:
            raise ValueError("Price is required for LIMIT and STOP_LIMIT orders.")

        try:
            price = float(price)
        except ValueError:
            raise ValueError("Price must be a number.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

        return price

    return None


def validate_stop_price(stop_price, order_type: str):
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValueError("stopPrice is required for STOP_LIMIT orders.")

        try:
            stop_price = float(stop_price)
        except ValueError:
            raise ValueError("stopPrice must be a number.")

        if stop_price <= 0:
            raise ValueError("stopPrice must be greater than zero.")

        return stop_price

    return None