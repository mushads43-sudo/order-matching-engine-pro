from flask import Flask, request, jsonify
from engine.matching_engine import MatchingEngine
from utils.logger import TradeLogger
from engine.order import Order

app = Flask(__name__)

logger = TradeLogger()
engine = MatchingEngine(logger)

order_counter = 1000  # starting ID for API orders

@app.route("/")
def home():
    return "🚀 Order Matching Engine API Running"

# 👉 Add Order API
@app.route("/order", methods=["POST"])
def add_order():
    global order_counter

    data = request.json

    try:
        order = Order(
            order_id=order_counter,
            stock=data["stock"],
            side=data["side"].upper(),
            price=float(data["price"]),
            quantity=int(data["quantity"])
        )

        order_counter += 1

        engine.add_order(order)

        return jsonify({"message": "Order added successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 👉 Get Trades API
@app.route("/trades", methods=["GET"])
def get_trades():
    trades_list = []

    for t in engine.trades:
        trades_list.append({
            "stock": t.stock,
            "price": t.price,
            "quantity": t.quantity,
            "buy_order_id": t.buy_order_id,
            "sell_order_id": t.sell_order_id
        })

    return jsonify(trades_list), 200


if __name__ == "__main__":
    app.run(debug=True)