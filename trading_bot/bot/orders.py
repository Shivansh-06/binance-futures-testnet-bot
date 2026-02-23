import logging
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
    validate_stop_price,
)
from bot.client import BinanceFuturesClient


logger = logging.getLogger(__name__)


def execute_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity,
    price=None,
    stop_price=None,
):
    """
    Main business logic for placing an order.
    """

    try:
        # Validate inputs
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)
        stop_price = validate_stop_price(stop_price, order_type)

        logger.info("Input validation successful.")

        # Initialize client
        client = BinanceFuturesClient()

        # Place order
        response = client.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price,
        )

        # Extract useful fields
        result = {
            "symbol": response.get("symbol"),
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A"),
            "side": response.get("side"),
            "type": response.get("type"),
        }

        logger.info(
            f"Order execution completed | OrderID={result['orderId']}"
        )

        return result

    except Exception as e:
        logger.error(f"Order execution failed: {str(e)}")
        raise