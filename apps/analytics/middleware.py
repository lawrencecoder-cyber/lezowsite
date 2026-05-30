from .trackers import ActivityTracker


class AnalyticsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.user.is_authenticated:
            ActivityTracker.track(
                user=request.user,
                action="page_view",
                metadata={"path": request.path}
            )

        return response
