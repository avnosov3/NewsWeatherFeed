## Описание проекта

Проект состоит из двух сервисов:
 1. Телеграм-бот. Бот сообщает пользователю о текущей погоде в интересующем его городе и выдаёт случайную новость.
 2. Веб-сервис. Веб-сервис позволяет пользователю просматривать историю отправленных ботом сообщений, а администратору - возможность просматривать статистику бота и редактировать сообщения, отправленные ботом.

### Телеграм-бот
Бот обрабатывает следующие команды:
* **/start** - бот приветствует пользователя и рассказывает о своих функциях
* **/help** - бот выводит пользователю список доступных команд
* **/weather [город]** - бот показывает пользователю текущую погоду в указанном им городе
* **/news** - бот отправляет пользователю случайную новость

### Веб-сервис
* http://127.0.0.1/telegram/ - страница с историей сообщений бота
* http://127.0.0.1/admin/ - страница администрирования бота


## Техно-стек

* python 3.10
* aiogram 2.25.1
* pydantic 1.8.2
* django 2.2.19
* drf 3.12.4
* gunicorn 21.0.4
* postgres 14.0
* psycopg2-binary 2.9.6
* nginx 1.19.3
* docker 20.10.16
* docker-compose 3.8

## Запуск проекта

1. Клонировать репозиторий и перейти в него в командной строке
```
git clone git@github.com:avnosov3/weather.git
cd weather/
```
2. Создать файл .env
```
DJANGO_KEY=<Указать секретный ключ>
DEBUG=True (если запуск в боевом режиме, то необходимо удалить переменную)

DB_ENGINE=django.db.backends.postgresql
DB_NAME=stone
POSTGRES_USER=<Указать имя пользователя>
POSTGRES_PASSWORD=<Указать пароль пользователя>
DB_HOST=db
DB_PORT=5432

TELEGRAM_TOKEN=5597408983:AAEROsD9jSDnxbKXDNpcfh_vHfXv92PI-Rs
WEATHER_TOKEN=18525583eb6a26d6db91bc189c6d5d87
NEWS_TOKEN=21145ed0c6e24777b09c25a9607b96df
COMMANDS_URL=http://web:8888/api/v1/info/
ANSWERS_URL=http://web:8888/api/v1/answers/
``` 

3. Запустить docker compose
```
docker compose up -d
```
4. Применить миграции
```
docker compose exec web poetry run python manage.py migrate
```
5. Создать супер-юзера
```
docker compose exec web poetry run python manage.py createsuperuser
```
6. Запустить бот  
  
    Ссылка на бот: https://t.me/CogniMateWeatherBot


* [История сообщений бота](http://127.0.0.1/telegram/)
* [Панель администратора](http://127.0.0.1/admin/)
* [Админка postgres](http://127.0.0.1/adminer/)