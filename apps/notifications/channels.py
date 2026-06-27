from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.stocks.websocket.broadcasters import StockBroadcaster

class NotificationChannel:

    GROUP_NAME = "notifications"

    @staticmethod
    def send(user_id, payload):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                "type": "notify.message",
                "data": payload,
            },
        )


class NotificationChannel:

    @staticmethod
    def send_stock_alert(alert_data):
        StockBroadcaster.broadcast({
            "type": "alert",
            "data": alert_data,
        })
