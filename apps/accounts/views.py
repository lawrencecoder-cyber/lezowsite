from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

from .forms import UserRegisterForm
from .services import AuthService
from .tokens import email_token_generator

User = get_user_model()


def register_view(request):
    """
    User registration with email verification.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # Create inactive user
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
                is_active=False,
            )

            # Send verification email
            AuthService.send_verification_email(user)

            return redirect("login")

    else:
        form = UserRegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def verify_email_view(request, uid, token):
    """
    Verify user email using token.
    """
    try:
        user = User.objects.get(pk=uid)

    except User.DoesNotExist:
        return redirect("login")

    if email_token_generator.check_token(user, token):
        user.is_active = True

        # Optional custom field
        if hasattr(user, "email_verified"):
            user.email_verified = True

        user.save()

        return redirect("login")

    return redirect("register")


def login_view(request):
    """
    User login view.
    """
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = AuthService.authenticate_user(
            request,
            username,
            password
        )

        if user:
            return redirect("home")

        error = "Invalid credentials"

    return render(
        request,
        "accounts/login.html",
        {"error": error}
    )


def logout_view(request):
    """
    User logout view.
    """
    AuthService.logout_user(request)

    return redirect("login")
