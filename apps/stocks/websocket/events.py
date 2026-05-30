class StockEventTypes:
    PRICE_UPDATE = "stock.price_update"
    NEWS_UPDATE = "stock.news_update"
    ALERT_TRIGGERED = "stock.alert"


class StockEvent:
    PRICE_UPDATE = "stock.price_update"
    NEWS_UPDATE = "stock.news_update"
    def __init__(self, event_type, payload):
        self.type = event_type
        self.payload = payload

    def to_dict(self):
        return {
            "type": self.type,
            "data": self.payload,
        }
