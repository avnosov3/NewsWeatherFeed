from rest_framework import mixins, viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import TelegramSerializer
from telegram.models import Telegram


class InfoCreateListViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Telegram.objects.all()
    serializer_class = TelegramSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('username', 'chat')
    ordering_fields = ('date',)
