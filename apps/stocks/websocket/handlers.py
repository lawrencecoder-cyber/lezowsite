from .events import StockEvent


class StockEventHandler:

    @staticmethod
    def handle_price_update(stock):
        return StockEvent(
            event_type="stock.price_update",
            payload={
                "symbol": stock.symbol,
                "price": str(stock.current_price),
                "change": str(stock.change),
                "percent_change": str(stock.percent_change),
            },
        ).to_dict()

    @staticmethod
    def handle_news_update(news):
        return StockEvent(
            event_type="stock.news_update",
            payload=news,
        ).to_dict()
