from django.db import models


class TelegramCommands(models.Model):
    username = models.CharField(
        max_length=256,
        verbose_name='Имя пользователя'
    )
    message = models.TextField(verbose_name='Команда пользователя')
    date = models.DateTimeField(verbose_name='Дата отправки сообщения')
    chat = models.CharField(
        max_length=256,
        verbose_name='Чат в котором отправили запрос',
        null=True
    )

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Использование команд бота'
        verbose_name_plural = 'Использование команд бота'

    OUT = (
        'username={username:.15} '
        'message={message:.12} '
        'date={date} '
        'chat={chat} '
    )

    def __str__(self):
        return self.OUT.format(
            username=self.username,
            message=self.message,
            date=self.date,
            chat=self.chat
        )


class CommandStatistics(models.Model):
    command_name = models.CharField(
        max_length=50, verbose_name='Название команды'
    )
    call_count = models.PositiveIntegerField(
        default=0, verbose_name='Количество вызовов'
    )

    class Meta:
        verbose_name = 'Статистика команды'
        verbose_name_plural = 'Статистика команд'

    def __str__(self):
        return f'У команды "{self.command_name}" нажатий "{self.call_count}"'


class BotAnswers(models.Model):
    username = models.CharField(
        max_length=256,
        verbose_name='Имя пользователя'
    )
    response = models.TextField(verbose_name='Ответ бота')
    date = models.DateTimeField(verbose_name='Дата отправки команды')

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Ответ бота'
        verbose_name_plural = 'Ответы бота'

    OUT = (
        'username={username:.15} '
        'message={response:.12} '
        'date={date} '
        'chat={chat} '
    )

    def __str__(self):
        return self.OUT.format(
            username=self.username,
            message=self.response,
            date=self.date,
        )
