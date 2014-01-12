from django.http import HttpRespose

def hello(request):
	return HttpResponse("Hi, World")