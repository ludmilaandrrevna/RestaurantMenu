from django.urls import path

from system.views import index, menu, orders


urlpatterns = [
    path('', index),
    path('menu/', menu),
    path('orders/', orders)
]
