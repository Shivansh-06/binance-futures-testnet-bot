import logging
import os


def setup_logging():
    """
    Configure logging for the trading bot.
    Logs are written to both console and file.
    """

    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "trading_bot.log")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-imported
    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)