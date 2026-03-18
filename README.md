# 📈 Order Matching Engine (HFT Simulation)

## 🧠 Overview
This project implements a **High-Frequency Trading (HFT) Order Matching Engine**, simulating how real-world stock exchanges match buy and sell orders.

It uses **price-time priority** to ensure fair and efficient execution, similar to production-grade trading systems used by financial institutions.

The system demonstrates **low-latency matching, efficient data structures, and thread-safe execution**.

---

## 🎯 Key Highlights
- Built a **real-time order matching engine** using price-time priority
- Implemented **heap-based order books** for efficient O(log n) operations
- Designed a **thread-safe system** using locks for concurrent execution
- Simulated **multi-stock trading environment**
- Developed **REST API** for real-time order submission and trade retrieval
- Enabled **bulk order processing via CSV using Pandas**
- Implemented **trade logging system** for tracking and auditing

---

## ⚙️ System Architecture

Matching Engine  
│  
├── Order Book  
│   ├── Buy Orders (Max Heap)  
│   └── Sell Orders (Min Heap)  
│  
├── Matching Logic  
├── Trade Execution  
└── Logging System  

---

## 🏗️ How It Works

1. **Order Submission**
   - Orders are submitted via REST API or CSV input
   - Each order includes:
     - Stock Symbol
     - Side (BUY / SELL)
     - Price
     - Quantity
     - Timestamp

2. **Order Book Storage**
   - Buy orders → stored in **Max Heap** (highest price first)
   - Sell orders → stored in **Min Heap** (lowest price first)

3. **Matching Logic**
   - Matching condition:
     ```
     Buy Price ≥ Sell Price
     ```
   - Orders matched using:
     - Best price priority
     - FIFO (time priority) within same price

4. **Trade Execution**
   - Trade quantity = minimum of buy/sell quantities
   - Partial fills supported
   - Remaining orders pushed back into heap

5. **Thread Safety**
   - Uses `threading.Lock` to ensure safe concurrent operations

6. **Trade Logging**
   - All executed trades stored and retrievable via API

---

## 🚀 Features
- Multi-stock support (AAPL, GOOG, MSFT)
- Price-Time Priority Matching
- Thread-safe execution
- Heap-based efficient order book
- Partial order fills
- CSV-based bulk order input (Pandas)
- REST API support
- Trade history tracking

---

## 🧰 Tech Stack

| Component        | Technology Used        |
|----------------|----------------------|
| Language        | Python               |
| Data Structures | Heap (Priority Queue)|
| Concurrency     | Threading + Locks    |
| Data Handling   | Pandas               |
| API             | FastAPI / Flask      |
| Logging         | Python Logging       |

---

## 📂 Project Structure
```
order-matching-engine/
│
├── engine/
│   ├── order.py
│   ├── order_book.py
│   ├── matching_engine.py
│   └── trade.py
│
├── api.py
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── orders.csv
│
├── screenshots/
│   ├── POST.png
│   └── GET.png
│
└── results/
    └── trades.csv
```


---

## ▶️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/order-matching-engine.git
cd order-matching-engine
## ⚙️ Setup Instructions

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the Project

### ▶️ Run Matching Engine (CLI)
```bash
python main.py
```

### Run REST API
```bash
python api.py
```

## 🌐 REST API

### 📌 Add Order

**Endpoint:**
```
POST /order
```

**Request Body:**
```json
{
  "stock": "AAPL",
  "side": "BUY",
  "price": 150,
  "quantity": 10
}
```

**Description:**
Adds a new order and triggers matching.

---

### 📌 Get Trades

**Endpoint:**
```
GET /trades
```

**Description:**
Returns all executed trades.

**Sample Response:**
```json
[
  {
    "stock": "AAPL",
    "price": 150,
    "quantity": 10,
    "timestamp": "2026-03-18T12:00:00"
  }
]
```

## 📸 Screenshots

### ➤ Add Order API

![Add Order](screenshots/POST.png)

### ➤ Trades Output

![Trades](screenshots/GET.png)

## 📊 Performance Considerations
- Heap operations ensure **O(log n)** complexity  
- Thread locks prevent **race conditions**  
- Efficient matching reduces latency (**HFT-style design**)  

---

## 🔮 Future Enhancements
- WebSocket support for real-time updates  
- Order cancellation and modification  
- Market orders & stop-loss orders  
- Redis/Kafka integration for scalability  
- Cloud deployment (AWS/GCP)  
- Latency benchmarking dashboard  

---

## 🧪 Example Workflow
1. Start API server  
2. Send BUY order *(price = 150)*  
3. Send SELL order *(price = 140)*  
4. Orders match instantly  
5. Trade stored and retrieved via `/trades`  

---

## 💼 Why This Project Matters
This project demonstrates:
- Market microstructure understanding  
- Low-latency system design  
- Strong DSA fundamentals  
- Concurrent programming skills  
- Real-world financial system simulation  
