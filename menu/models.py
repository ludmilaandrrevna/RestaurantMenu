from django.db import models
from django.contrib import admin


class Component(models.Model):
    name = models.CharField(max_length=40)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return '{}, weight = {}, price = {}'.format(
            self.name,
            self.weight,
            self.price
        )


class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price')


class Dish(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    components = models.ManyToManyField(Component)

    def _calculate_weight(self):
        weight_sum = 0
        for component in self.components.all():
            weight_sum += component.weight
        return weight_sum

    weight = property(_calculate_weight)

    def __str__(self):
        return self.name


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weight')


class Order(models.Model):
    dishes = models.ManyToManyField(Dish)

    def _calculate_price(self):
        price = 0
        for dish in self.dishes.all():
            price += dish.price
        return price

    price = property(_calculate_price)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')


