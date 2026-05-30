from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Stock
from .serializers import StockSerializer
from apps.api.throttling import BurstRateThrottle, SustainedRateThrottle


class StockViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [BurstRateThrottle, SustainedRateThrottle]
