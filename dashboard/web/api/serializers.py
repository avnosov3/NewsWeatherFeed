from rest_framework import serializers

from telegram.models import Telegram


class TelegramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telegram
        fields = (
            'username', 'message', 'date', 'chat'
        )
