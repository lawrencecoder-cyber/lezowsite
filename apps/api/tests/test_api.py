from django.test import TestCase
from rest_framework.test import APIClient


class APITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_stocks_endpoint(self):
        response = self.client.get("/api/v1/stocks/")
        self.assertEqual(response.status_code, 200)
