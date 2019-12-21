from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import RegisterForm

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
			messages.success(request, 'Bienvenido {}'.format(user.username))
			return redirect('index')
		else:
			messages.error(request, 'Usuario o contraseña no válidos')
 
	return render(request, 'users/login.html', {

	})

def logout_view(request):
	logout(request)
	messages.success(request, 'Sesión cerrada exitosamente')
	return redirect('login')

def register(request):
	# form = RegisterForm({
	# 	'username': 'pulidovpe',
	# 	'email': 'pulidovpe.dev@gmail.com'
	# })
	form = RegisterForm(request.POST or None)

	if request.method == 'POST' and form.is_valid():
		username = form.cleaned_data.get('username')		## Dic
		email    = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')

		print(username)
		print(email)
		print(password)

	return render(request, 'users/register.html', {
		'form': form
	})