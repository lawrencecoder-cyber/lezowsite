from urllib.parse import parse_qs


class WebSocketAuthMiddleware:

    """
    Future-ready middleware for:
    - token auth
    - user validation
    - subscription filtering
    """

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_string = scope.get("query_string", b"").decode()
        params = parse_qs(query_string)

        scope["user_token"] = params.get("token", [None])[0]

        return await self.app(scope, receive, send)
