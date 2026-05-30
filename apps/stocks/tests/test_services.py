from django.test import TestCase
from ..services.indicators import calculate_sma


class IndicatorTest(TestCase):

    def test_sma(self):
        result = calculate_sma([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 4)
