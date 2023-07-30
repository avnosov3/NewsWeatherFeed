from django.shortcuts import render
from .models import BotAnswers


def index(request):
    user_filter = request.GET.get('user')
    messages = BotAnswers.objects.all()
    if user_filter:
        messages = BotAnswers.objects.filter(username__icontains=user_filter)
    return render(request, 'index.html', dict(messages=messages))
