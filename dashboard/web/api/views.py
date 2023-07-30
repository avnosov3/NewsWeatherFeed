from rest_framework import mixins, viewsets

from .serializers import TelegramSerializer, BotAnsersSetializer
from telegram.models import TelegramCommands, BotAnswers


class InfoCreateListViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = TelegramCommands.objects.all()
    serializer_class = TelegramSerializer


class AnswersCreateListViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = BotAnswers.objects.all()
    serializer_class = BotAnsersSetializer
