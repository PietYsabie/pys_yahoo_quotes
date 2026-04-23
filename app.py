from flask import Flask, request, jsonify
from yahoo_fin.stock_info import get_live_price

app = Flask(__name__)

@app.route("/price")
def price():
    ticker = request.args.get("ticker")
    if not ticker:
        return jsonify({"error": "No ticker provided"})
    try:
        price = get_live_price(ticker)
        return jsonify({"price": price})
    except Exception as e:
        return jsonify({"error": str(e)})

# nodig voor deployment
if __name__ == "__main__":
    app.run()