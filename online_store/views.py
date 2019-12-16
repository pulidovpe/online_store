from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth import authenticate
from django.contrib.auth import login

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

def login_view(request):
	##print(request.method)
	if request.method == 'POST':
		username = request.POST.get('username')	## diccionario
		password = request.POST.get('password')	## None

		user = authenticate(username=username, password=password) ## None
		if user:
			login(request, user)
			return redirect('index')
		else:
			print('Usuario No autenticado')
 

	return render(request, 'users/login.html', {

	})