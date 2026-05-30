from .websocket.broadcasters import StockBroadcaster


class StockWebSocketService:

    @staticmethod
    def push_update(stock):
        StockBroadcaster.broadcast_price_update(stock)
