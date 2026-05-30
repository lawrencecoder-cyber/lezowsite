from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from .tokens import email_token_generator

User = get_user_model()


class AuthService:
    @staticmethod
    def register_user(form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return user

    @staticmethod
    def authenticate_user(request, username, password):
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return user

    @staticmethod
    def send_verification_email(user):
        token = email_token_generator.make_token(user)

        verification_link = f"{settings.FRONTEND_URL}/verify/{user.pk}/{token}/"

        send_mail(
            subject="Verify your account",
            message=f"Click to verify: {verification_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

    @staticmethod
    def logout_user(request):
        logout(request)
