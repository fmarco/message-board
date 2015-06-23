from .views import MessageViewSet
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
