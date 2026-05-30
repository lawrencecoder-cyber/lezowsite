from celery import shared_task

from apps.stocks.services.market_data import MarketDataService
from apps.stocks.websocket.handlers import StockEventHandler
from apps.stocks.websocket.broadcasters import StockBroadcaster


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 5},
)
def update_all_stock_prices(self):
    """
    Fetch latest stock prices, update database, and broadcast updates via WebSockets.
    """
    service = MarketDataService()

    # Bulk update returns updated stock objects
    updated_stocks = service.bulk_update()

    results = []

    for stock in updated_stocks:
        # Convert stock update into WebSocket event
        event = StockEventHandler.handle_price_update(stock)

        # Broadcast to connected clients
        StockBroadcaster.broadcast(event)

        results.append(event)

    return {
        "status": "success",
        "updated_count": len(results),
    }
