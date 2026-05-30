from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class HybridAuth(SessionAuthentication, TokenAuthentication):
    """
    Authentication class supporting:

    - Django session authentication (web/browser)
    - DRF token authentication (API clients)
    """
    pass


class HybridJWTAuth(JWTAuthentication, SessionAuthentication):
    """
    Authentication class supporting:

    - JWT authentication (mobile/API)
    - Django session authentication (web/browser)
    """
    pass
