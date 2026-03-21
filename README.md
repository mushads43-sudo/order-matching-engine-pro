# Order Matching Engine (HFT Simulation)

## **Overview**

This project implements a High-Frequency Trading (HFT) Order Matching Engine that simulates how real-world stock exchanges match buy and sell orders.

It uses price-time priority to ensure fair and efficient execution, closely resembling production-grade trading systems used in financial markets. The system highlights low-latency processing, efficient data structures, and thread-safe execution.

---

## **Problem Statement**

Financial markets require extremely fast and reliable systems to match buy and sell orders in real time. Traditional implementations may struggle with scalability, latency, and concurrency.

This project solves these challenges by:
- Designing an efficient order matching mechanism using price-time priority  
- Ensuring low-latency execution with optimized data structures  
- Handling concurrent order submissions safely using thread synchronization  
- Simulating real-world trading scenarios for multiple stocks  

---

## **Tech Stack**

- Programming: Python  
- Data Structures: Heap (Priority Queue)  
- Concurrency: Threading, Locks  
- Data Processing: Pandas  
- API Development: FastAPI / Flask  
- Logging: Python Logging  

---

## **Approach**

### **Data Collection and Input Handling**
- Accepted orders via REST API and CSV files  
- Each order includes stock symbol, side, price, quantity, and timestamp  
- Used Pandas for bulk order processing  

---

### **Feature Engineering / System Design**
- Designed separate order books for buy and sell sides  
- Buy orders stored in Max Heap (highest price priority)  
- Sell orders stored in Min Heap (lowest price priority)  
- Maintained FIFO order within same price level  

---

### **Model Building (System Logic)**

- **Order Matching Engine:**
  - Implemented price-time priority logic  
  - Matching condition: Buy Price ≥ Sell Price  

- **Execution Engine:**
  - Supports partial order fills  
  - Calculates trade quantity dynamically  
  - Updates remaining orders back into heap  

- **Concurrency Handling:**
  - Used threading locks for safe parallel execution  

- **API Layer:**
  - Built REST endpoints for order submission and trade retrieval  

---

### **Evaluation**

- Verified correctness of matching logic under multiple scenarios  
- Tested system with bulk orders and concurrent requests  
- Measured efficiency using heap-based operations (O(log n))  
- Ensured thread safety by preventing race conditions  

---

## **Results**

- Successfully implemented a real-time order matching engine  
- Achieved efficient order processing using heap-based structures  
- Ensured accurate trade execution with support for partial fills  
- Enabled concurrent order handling using thread-safe mechanisms  
- Built a functional API for real-time trading simulation  

---

## **Output**

- Real-time order matching and trade execution  
- Trade history retrieval via API  
- CSV-based trade logs for analysis  
- Multi-stock trading simulation  
- REST API endpoints for interaction  

---

## **How to Run**

```bash
git clone https://github.com/YOUR_USERNAME/order-matching-engine.git
cd order-matching-engine

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
python main.py
```
## **Key Learning**

- Built a real-time order matching engine using price-time priority logic  
- Gained strong understanding of market microstructure and trading systems 
- Implemented heap-based data structures for efficient O(log n) operations  
- Learned concurrent programming using threading and locks  
- Designed REST APIs for real-time system interaction  
- Handled bulk data processing using Pandas  
- Developed scalable and low-latency system architecture  
- Strengthened problem-solving skills in data structures and system design  
- Simulated real-world financial systems with practical implementation  
