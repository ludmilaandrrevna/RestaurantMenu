from django.db import models
from django.utils.translation import gettext_lazy as _


class Component(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    weight = models.IntegerField(verbose_name=_('weight'))
    price = models.IntegerField(verbose_name=_('price'))

    class Meta:
        verbose_name = _('component')
        verbose_name_plural = _('components')

    def __str__(self):
        return str(self.title)


class Dish(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    price = models.IntegerField(verbose_name=_('price'))

    class Meta:
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')

    def weight(self):
        if not hasattr(self, 'recipe'):
            return 'N/A'
        return sum([
            component.weight
            for component in self.recipe.components.all()
        ])

    weight.short_description = _('weight')

    def __str__(self):
        return self.title


class Recipe(models.Model):
    dish = models.OneToOneField(
        'Dish',
        on_delete=models.CASCADE,
        verbose_name=_('dish'),
        primary_key=True
    )
    components = models.ManyToManyField(
        'Component', 
        verbose_name=_('components')
    )
    time = models.DurationField(verbose_name=_('time'))
    complexity = models.CharField(
        max_length=10, 
        verbose_name=_('complexity'), 
        choices=[
            ('1', _('Newbie')),
            ('2', _('Middle')),
            ('3', _('Master')),
        ]
    )

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')

    def __str__(self):
        return str(self.dish.title)


class Order(models.Model):
    table_num = models.IntegerField(verbose_name=_('table_num'))
    dishes = models.ManyToManyField('Dish', verbose_name=_('dishes'))
    time = models.DateTimeField(auto_now=True, verbose_name=_('time'))

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def price(self):
        return sum([dish.price for dish in self.dishes.all()])

    price.short_description = _('price')
