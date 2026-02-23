import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException


logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    """
    Wrapper around Binance Futures Testnet client.
    """

    def __init__(self):
        load_dotenv()

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found in environment variables.")

        self.client = Client(api_key, api_secret)

        # Override base URL to Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logger.info("Binance Futures Testnet client initialized successfully.")

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: float = None,
        stop_price: float = None,
    ):
        """
        Place an order on Binance Futures Testnet.
        """

        try:
            logger.info(
                f"Placing order | Symbol={symbol} | Side={side} | "
                f"Type={order_type} | Quantity={quantity} | "
                f"Price={price} | StopPrice={stop_price}"
            )

            params = {
                "symbol": symbol,
                "side": side,
                "quantity": quantity,
            }

            # MARKET ORDER
            if order_type == "MARKET":
                params["type"] = "MARKET"

            # LIMIT ORDER
            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders.")

                params["type"] = "LIMIT"
                params["price"] = price
                params["timeInForce"] = "GTC"

            # STOP-LIMIT ORDER
            elif order_type == "STOP_LIMIT":
                if price is None or stop_price is None:
                    raise ValueError(
                        "Both price and stopPrice are required for STOP_LIMIT."
                    )

                params["type"] = "STOP"
                params["price"] = price
                params["stopPrice"] = stop_price
                params["timeInForce"] = "GTC"

            else:
                raise ValueError("Unsupported order type.")

            response = self.client.futures_create_order(**params)

            logger.info(
                f"Order placed successfully | OrderID={response.get('orderId')}"
            )
            logger.debug(f"Full response: {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceRequestException as e:
            logger.error(f"Network error: {str(e)}")
            raise

        except Exception:
            logger.exception("Unexpected error occurred while placing order.")
            raise