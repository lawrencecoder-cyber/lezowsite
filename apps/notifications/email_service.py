from django.core.mail import send_mail
from django.conf import settings


class EmailService:

    @staticmethod
    def send_alert_email(user_email, message):
        send_mail(
            subject="Stock Alert",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=True,
        )
