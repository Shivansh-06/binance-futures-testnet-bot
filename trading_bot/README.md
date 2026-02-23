# Binance Futures Testnet Trading Bot

A simplified trading bot built in Python that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## Features

- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input using argparse
- Structured architecture (client, validation, business logic)
- Proper logging (console + file)
- Error handling for API and input validation

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
│
├── cli.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd trading_bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file inside the `trading_bot` directory:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key
```

---

## Usage Examples

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.003
```

MARKET Order Log
2026-02-23 19:15:42 | INFO | bot.client | Placing order | Symbol=BTCUSDT | Type=MARKET | Quantity=0.003
2026-02-23 19:15:43 | INFO | bot.orders | Order execution completed | OrderID=123456789

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.003 --price 40000
```
LIMIT Order Log
2026-02-23 19:18:10 | INFO | bot.client | Placing order | Symbol=BTCUSDT | Type=LIMIT | Quantity=0.003 | Price=40000
2026-02-23 19:18:11 | INFO | bot.orders | Order execution completed | OrderID=987654321

---

### STOP_LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.003 --price 66000 --stop-price 67000
```




## Logging

Logs are saved in:

```
trading_bot/logs/trading_bot.log
```

Logs include:

- Order requests
- Order responses
- Errors
- Validation failures

---

## Assumptions

- Binance Futures Testnet account is configured
- Minimum notional requirement (100 USDT) is respected
- Python 3.10+ environment
- user provides their own api credentials
- STOP_LIMIT orders must include both --price and --stop-price

---

## Dependencies

- python-binance
- python-dotenv

---

## Author

Built as part of an internship evaluation task.
