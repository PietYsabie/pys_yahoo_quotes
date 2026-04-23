from flask import Flask, request, jsonify
from yahoo_fin.stock_info import get_data
import traceback
import requests

app = Flask(__name__)



@app.route("/price")
def price():
    ticker = request.args.get("ticker")
    
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    
    try:
        data = res.json()
        price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        return jsonify({"price": price})
    except:
        return jsonify({
            "error": "Yahoo blocked or invalid response",
            "raw": res.text[:200]
        })


