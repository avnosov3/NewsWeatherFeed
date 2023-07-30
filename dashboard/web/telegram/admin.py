from django.contrib import admin
from .models import TelegramCommands, CommandStatistics, BotAnswers
from django.db.models import Count


@admin.register(TelegramCommands)
class TelegramCommandsAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'message', 'date', 'chat'
    )
    readonly_fields = ('username',)
    list_display_links = ('message',)
    search_fields = ('username', 'message')
    list_filter = ('username', 'chat')
    empty_value_display = '-пусто-'


@admin.register(CommandStatistics)
class CommandStatisticsAdmin(admin.ModelAdmin):
    list_display = ('command_name', 'call_count')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        unique_commands = TelegramCommands.objects.values(
            'message'
        ).annotate(
            count=Count('username')
        ).order_by('-count')

        for command in unique_commands:
            command_name = command['message']
            call_count = command['count']
            command_stat, created = CommandStatistics.objects.get_or_create(
                command_name=command_name,
                defaults={'call_count': call_count}
            )
            if not created:
                command_stat.call_count = call_count
                command_stat.save()

        return CommandStatistics.objects.all()


@admin.register(BotAnswers)
class BotAnswersAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'response', 'date'
    )
    readonly_fields = ('username',)
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'
