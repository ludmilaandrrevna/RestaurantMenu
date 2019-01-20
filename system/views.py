from django.shortcuts import render

from system.models import Dish, Order


def index(request):
	return render(request, 'system/index.html', {})


def menu(request):
	dishes = Dish.objects.all()
	return render(request, 'system/menu.html', {
		'dishes': dishes
	})


def orders(request):
	orders = Order.objects.all()
	return render(request, 'system/orders.html', {
		'orders': orders
	})
