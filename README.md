# 📈 Order Matching Engine (HFT Simulation)

## Overview
This project implements a high-performance Order Matching Engine, simulating the core functionality of modern electronic stock exchanges used in high-frequency trading (HFT) systems.
The engine processes buy and sell orders using price-time priority, ensuring fair and deterministic trade execution. It is designed with thread safety, scalability, and real-time processing in mind—key requirements in financial trading systems.

## Features
- Simulates real-world exchange matching logic
- Thread-safe architecture for concurrent order processing
- Handles multi-stock trading environments
- Supports bulk order ingestion via CSV
- Implements price-time priority (FIFO within same price)
- Maintains detailed trade logs for auditability
- Exposes a simple REST API for interaction

## System Architecture
User/API → Matching Engine → Order Book → Trade Execution → Logging

## Tech Stack
| Component       | Technology             |
| --------------- | ---------------------- |
| Language        | Python                 |
| Data Structures | Heap (Priority Queue)  |
| Concurrency     | Threading (Lock-based) |
| Data Handling   | Pandas                 |
| API             | Flask                  |
| Logging         | Python Logging         |

## Matching Logic (Core Concept)
- Orders are inserted into buy/sell heaps
- Matching occurs when buy price >= sell price
- Trades executed using FIFO within same price
The engine follows Price-Time Priority, the industry-standard mechanism:
1. Buy orders are matched with the lowest available sell price
2. A trade executes when:
Buy Price ≥ Sell Price
3. If multiple orders exist at the same price:
The earliest order (FIFO) is executed first
EXAMPLE:
| Order Type | Price | Quantity |
| ---------- | ----- | -------- |
| BUY        | 150   | 10       |
| SELL       | 145   | 10       |
✅ Trade executes at 145 (sell price)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/order-matching-engine.git
cd order-matching-engine

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Running the Engine
Run Core Engine
python main.py

Run REST API
python api.py

🌐 REST API
Base URL
http://127.0.0.1:5000

📌 Endpoints
➤ Add Order
POST /order
Request Body:
{
  "stock": "AAPL",
  "side": "BUY",
  "price": 150,
  "quantity": 10
}
Features:
Supports multiple stocks (AAPL, GOOG, MSFT)
Automatically triggers matching after insertion

➤ Get Trades
GET /trades
Response:
[
  {
    "stock": "AAPL",
    "price": 145,
    "quantity": 10,
    "timestamp": "2026-03-18T12:00:00"
  }
]

➤ Bulk Order Upload (Optional Enhancement)
Upload CSV file containing multiple orders:
stock,side,price,quantity
AAPL,BUY,150,10
AAPL,SELL,145,10

## 📸 Screenshots

### ➤ Add Order API

![Add Order](screenshots/POST.png)

### ➤ Trades Output

![Trades](screenshots/GET.png)

order-matching-engine/
│
├── engine/
│   ├── matching_engine.py
│   ├── order_book.py
│   ├── order.py
│   └── trade.py
│
├── api.py
├── main.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── POST.png
    └── GET.png

## Concurrency & Thread Safety
Uses threading.Lock() to ensure:
Atomic order insertion
Safe matching execution
Prevents race conditions in concurrent environments

## Logging & Audit
Every trade is logged with:
Price
Quantity
Timestamp
Enables traceability and debugging, critical for financial systems

## Future Enhancements
⏱️ Latency benchmarking (microsecond-level)
📉 Order cancellation & modification
📊 Real-time dashboard (Streamlit / React)
⚡ Async processing (Kafka / RabbitMQ)
💾 Database integration (PostgreSQL)
📡 WebSocket-based live order feed
