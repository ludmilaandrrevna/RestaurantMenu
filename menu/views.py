from django.shortcuts import render

from menu.models import Dish, Order


def index(request):
	return render(request, 'menu/index.html', {})


def menu(request):
	dishes = Dish.objects.all()
	return render(request, 'menu/menu.html', {
		'dishes': dishes
	})


def orders(request):
	orders = Order.objects.all()
	return render(request, 'menu/orders.html', {
		'orders': orders
	})
