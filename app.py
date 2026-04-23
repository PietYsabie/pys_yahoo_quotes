from flask import Flask, request, jsonify
from yahoo_fin.stock_info import get_data
import traceback

app = Flask(__name__)

@app.route("/price")
def price():
    ticker = request.args.get("ticker")
    
    try:
        df = get_data(ticker, interval="1d", index_as_date=False)
        price = df.iloc[-1]["close"]
        return jsonify({"price": float(price)})
    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        })
# nodig voor deployment
if __name__ == "__main__":
    app.run()


    



