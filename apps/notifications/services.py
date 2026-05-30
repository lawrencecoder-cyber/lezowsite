from .models import Notification


class NotificationService:

    @staticmethod
    def create_notification(user, message):
        return Notification.objects.create(
            user=user,
            message=message
        )
