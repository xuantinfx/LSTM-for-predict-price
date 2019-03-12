# Flask Server dùng để predict giá của BTC/USDT
- Thuật toán dùng là LSTM
- Dựa trên [Model](https://github.com/jaungiers/LSTM-Neural-Network-for-Time-Series-Prediction)
# Cách chạy (Windows)
1. `pip install -r requirements.txt`
2. `set FLASK_APP=flask_server.py`
3. `set FLASK_ENV=development` or `set FLASK_ENV=production`
4. `py flask -m run`
# Cách dùng
- API `http://127.0.0.1:5000/advice?start={time_unix*1000}&open={open}&high={high}&low={low}}&close={close}&vwp={vwp}&volume={volume}&trades={trades}&macd={macd}&rsi={rsi}`
- Example: [http://127.0.0.1:5000/advice?start=1551930660000&open=3882.92&high=3885.84&low=3882.92&close=3884.28&vwp=3884.1946284686705&volume=6.044644999999998&trades=53&macd=-0.6522559909219352&rsi=0](http://127.0.0.1:5000/advice?start=1551930660000&open=3882.92&high=3885.84&low=3882.92&close=3884.28&vwp=3884.1946284686705&volume=6.044644999999998&trades=53&macd=-0.6522559909219352&rsi=0)

# Lưu ý
- Mỗi lần gọi advice thì candle sẽ tự động được lưu vào file `model/data/BTC_USDT_RSI_MACD.csv`