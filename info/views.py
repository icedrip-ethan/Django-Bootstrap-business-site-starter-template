from django.shortcuts import render

def index(request):
	return render(request, 'info/home.html')
def about(request):
	return render(request, 'info/about.html')
def services(request):
	return render(request, 'info/services.html')
def resources(request):
	return render(request, 'info/resources.html')