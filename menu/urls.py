from django.urls import path

from menu.views import index, menu, orders


urlpatterns = [
    path('', index),
    path('menu/', menu),
    path('orders/', orders)
]
