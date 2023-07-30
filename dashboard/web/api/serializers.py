from rest_framework import serializers

from telegram.models import TelegramCommands, BotAnswers


class TelegramSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelegramCommands
        fields = (
            'username', 'message', 'date', 'chat'
        )


class BotAnsersSetializer(serializers.ModelSerializer):

    class Meta:
        model = BotAnswers
        fields = (
            'username', 'response', 'date'
        )
