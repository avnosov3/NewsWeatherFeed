from django.shortcuts import render
from .models import Telegram


def index(request):
    user_filter = request.GET.get('user')
    chat_filter = request.GET.get('chat')
    messages = Telegram.objects.all()
    if user_filter:
        messages = Telegram.objects.filter(username__icontains=user_filter)
    if chat_filter:
        messages = Telegram.objects.filter(chat__icontains=chat_filter)
    return render(request, 'index.html', dict(messages=messages))
