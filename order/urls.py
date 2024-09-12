from django.urls import path, include
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(r'order', viewsets.orderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]