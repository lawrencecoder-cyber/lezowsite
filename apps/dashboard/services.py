from .selectors import DashboardSelector


class DashboardService:

    @staticmethod
    def build_dashboard_context():
        return {
            "top_stocks": DashboardSelector.get_top_stocks(),
            "movers": DashboardSelector.get_movers(),
        }
