from apps.notifications.models import PriceAlert
from apps.notifications.services import NotificationService
from apps.notifications.channels import NotificationChannel


class AlertEngine:
    """
    Handles evaluation and triggering of price-based stock alerts.
    """

    @staticmethod
    def evaluate_stock(stock):
        """
        Evaluate alerts for a single stock instance.
        """
        alerts = PriceAlert.objects.filter(
            stock=stock,
            is_active=True
        )

        for alert in alerts:
            if stock.current_price >= alert.target_price:
                AlertEngine.trigger(alert, stock)

    @staticmethod
    def evaluate_all():
        """
        Evaluate all active alerts in the system.
        """
        alerts = PriceAlert.objects.filter(is_active=True).select_related("stock")

        for alert in alerts:
            stock = alert.stock

            if stock.current_price >= alert.target_price:
                AlertEngine.trigger(alert, stock)

    @staticmethod
    def trigger(alert, stock):
        """
        Trigger notification for a fulfilled alert.
        """
        message = (
            f"{stock.symbol} has reached {stock.current_price} "
            f"(target: {alert.target_price})"
        )

        # Create internal notification
        NotificationService.create_notification(alert.user, message)

        # Send real-time/channel notification
        NotificationChannel.send(alert.user.id, {
            "type": "price_alert",
            "symbol": stock.symbol,
            "current_price": str(stock.current_price),
            "target_price": str(alert.target_price),
            "message": message,
        })

        # Deactivate alert after triggering
        alert.is_active = False
        alert.save(update_fields=["is_active"])
