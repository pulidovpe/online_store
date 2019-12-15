from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	##return HttpResponse('Hola Mundo!')
	return render(request,'index.html',{
		'message0': 'Nuevo mensaje (de contexto) desde la vista',
		'message1': 10 + 20,
		'message2': [1,2,3],
		'message3': True,
	})