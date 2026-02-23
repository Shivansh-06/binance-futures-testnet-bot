import argparse
import logging

from bot.logging_config import setup_logging
from bot.orders import execute_order


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g., BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order side (BUY or SELL)",
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT", "STOP_LIMIT"],
        help="Order type (MARKET or LIMIT)",
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order quantity",
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (required for LIMIT orders)",
    )

    parser.add_argument(
    "--stop-price",
    type=float,
    help="Stop price (required for STOP_LIMIT orders)",
    )

    return parser.parse_args()


def main():
    setup_logging()
    args = parse_arguments()

    try:
        print("\n===== ORDER REQUEST =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")

        result = execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
            stop_price=args.stop_price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID     : {result['orderId']}")
        print(f"Status       : {result['status']}")
        print(f"Executed Qty : {result['executedQty']}")
        print(f"Avg Price    : {result['avgPrice']}")

        print("\n✅ Order placed successfully.")

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        print("\n❌ Order failed. Check logs for details.")


if __name__ == "__main__":
    main()