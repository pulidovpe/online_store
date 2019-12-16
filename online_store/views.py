from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	##return HttpResponse('Hola Mundo!')
	return render(request,'index.html',{
		'message': 'Listado de productos',
		'title'  : 'Productos',
		'products'  : [
			{'title': 'Playera', 'price': '5', 'stock': True},
			{'title': 'Camisa', 'price': '7', 'stock': True},
			{'title': 'Mochila', 'price': '20', 'stock': False},
			{'title': 'Laptop', 'price': '500', 'stock': True},
		]
	})

def login(request):
	return render(request, 'users/login.html', {
		#
	})