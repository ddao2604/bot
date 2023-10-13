import websocket, json, pprint, numpy
from binance.client import Client
from binance.enums import *

SOCKET = "wss://dstream.binance.com/stream?streams=ethusdt@kline_15m"
client = Client("", "", tld='us')
   
def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    
    json_message = json.loads(message)
    #pprint.pprint(json_message)
    candle = json_message['k']
    oprice = candle['o']
    close = candle['c']
    print("Open "+oprice+ " - Close "+close)
        

                
ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()
