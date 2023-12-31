# Generated by Django 2.2.19 on 2023-07-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, verbose_name='Имя пользователя')),
                ('response', models.TextField(verbose_name='Ответ бота')),
                ('date', models.DateTimeField(verbose_name='Дата отправки команды')),
            ],
            options={
                'verbose_name': 'Ответ бота',
                'verbose_name_plural': 'Ответы бота',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='CommandStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command_name', models.CharField(max_length=50, verbose_name='Название команды')),
                ('call_count', models.PositiveIntegerField(default=0, verbose_name='Количество вызовов')),
            ],
            options={
                'verbose_name': 'Статистика команды',
                'verbose_name_plural': 'Статистика команд',
            },
        ),
        migrations.CreateModel(
            name='TelegramCommands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, verbose_name='Имя пользователя')),
                ('message', models.TextField(verbose_name='Команда пользователя')),
                ('date', models.DateTimeField(verbose_name='Дата отправки сообщения')),
                ('chat', models.CharField(max_length=256, null=True, verbose_name='Чат в котором отправили запрос')),
            ],
            options={
                'verbose_name': 'Использование команд бота',
                'verbose_name_plural': 'Использование команд бота',
                'ordering': ('-date',),
            },
        ),
    ]
