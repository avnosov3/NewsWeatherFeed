from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InfoCreateListViewSet, AnswersCreateListViewSet

router_v1 = DefaultRouter()
router_v1.register(r'info', InfoCreateListViewSet, 'create-telegram-info')
router_v1.register(r'answers', AnswersCreateListViewSet, 'create-answers')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
