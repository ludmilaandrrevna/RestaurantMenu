from django.contrib import admin

from menu.models import Dish, Component, Menu, DishAdmin, MenuAdmin


admin.site.register(Component)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)
