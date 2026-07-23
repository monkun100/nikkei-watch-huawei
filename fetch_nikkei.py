import json
from datetime import datetime, timedelta, timezone

import yfinance as yf


def fetch_nikkei():
    ticker = yf.Ticker("^N225")
    fast_info = ticker.fast_info

    current_price = fast_info["last_price"]
    prev_close = fast_info["previous_close"]
    change = current_price - prev_close
    change_percent = (change / prev_close) * 100

    jst = timezone(timedelta(hours=9))
    now = datetime.now(jst)

    data = {
        "updated_at": now.strftime("%Y-%m-%d %H:%M:%S"),
        "price": round(float(current_price), 2),
        "prev_close": round(float(prev_close), 2),
        "change": round(float(change), 2),
        "change_percent": round(float(change_percent), 2),
    }

    with open("nikkei.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"日経平均: {data['price']} ({data['change']:+.2f}, {data['change_percent']:+.2f}%)")
    print("nikkei.json に保存しました")


if __name__ == "__main__":
    fetch_nikkei()
