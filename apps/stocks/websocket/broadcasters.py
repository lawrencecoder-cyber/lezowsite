from typing import Any

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class StockBroadcaster:
    """
    Handles WebSocket broadcasting for stock events.
    """

    GROUP_NAME = "stocks"

    @classmethod
    def broadcast(cls, event_type: str, data: dict[str, Any]) -> None:
        """
        Send an event to all connected stock clients.

        Args:
            event_type: Channels event handler type.
            data: Payload to broadcast.
        """
        channel_layer = get_channel_layer()

        if channel_layer is None:
            return

        async_to_sync(channel_layer.group_send)(
            cls.GROUP_NAME,
            {
                "type": event_type,
                "data": data,
            },
        )

    @classmethod
    def broadcast_price_update(cls, stock) -> None:
        """
        Broadcast stock price updates.
        """
        cls.broadcast(
            event_type="stock.update",
            data={
                "symbol": stock.symbol,
                "price": str(stock.current_price),
                "change": str(stock.change),
                "percent": str(stock.percent_change),
            },
        )
