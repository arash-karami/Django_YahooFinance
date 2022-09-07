from re import L
import yfinance as yf
import json


msft = yf.Ticker("MSFT")
hist = msft.history(period = "1mo", interval = "1d")
hist=hist.reset_index()
hist= hist.reset_index()
#hist = hist['Close'].to_json()
#hist=json.loads(hist)

#hist=hist.get('Close','Date')

x =hist[['index','Close']].values


for i , m in x:

    print (i , m)

