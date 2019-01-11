from django.contrib import admin

from menu.models import Dish, Component, Order, DishAdmin, OrderAdmin, ComponentAdmin


admin.site.register(Component, ComponentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Dish, DishAdmin)
