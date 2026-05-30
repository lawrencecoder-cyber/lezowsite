from django.test import TestCase
from apps.dashboard.selectors import DashboardSelector


class DashboardTest(TestCase):

    def test_top_stocks(self):
        result = DashboardSelector.get_top_stocks()
        self.assertTrue(hasattr(result, "order_by"))
