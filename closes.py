import websocket, json, pprint, talib, numpy
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/xmrbtc@kline_5m"

closes = []
in_position = False

client = Client(<>, <>, tld='com')


def on_open(ws):
    print('opened connection')


def on_close(ws):
    print('closed connection')


def on_message(ws, message):
    global closes, in_position

    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']


    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)
    

