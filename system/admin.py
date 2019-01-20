from django.contrib import admin
from django.utils.translation import gettext as _

from system import models

admin.site.index_title = _('My Index Title')
admin.site.site_header = _('My Site Administration')
admin.site.site_title = _('My Site Management')


class ComponentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'weight', 'price']
    search_fields = ['title']


class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'weight']
    search_fields = ['title']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['dish', 'complexity', 'time']
    list_filter = ['components', 'complexity']
    search_fields = ['dish__title']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'table_num', 'price', 'time']
    list_filter = ['table_num']


admin.site.register(models.Component, ComponentAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Dish, DishAdmin)
admin.site.register(models.Order, OrderAdmin)
