from .views import MessageViewSet
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'', MessageViewSet)

urlpatterns = [
    url(r'^messages', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^$', TemplateView.as_view(template_name='index.html'))
]