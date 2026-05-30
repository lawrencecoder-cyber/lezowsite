from .models import UserActivity

class EventTypes:
    LOGIN = "login"
    VIEW_STOCK = "view_stock"
    ADD_WATCHLIST = "add_watchlist"
    SET_ALERT = "set_alert"

class ActivityTracker:

    @staticmethod
    def track(user, action, metadata=None):
        return UserActivity.objects.create(
            user=user,
            action=action,
            metadata=metadata or {}
        )
