from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def info(request):
  return render(request, 'info.html')

def about_us(request):
  return render(request, 'about-us.html')

def contact(request):
  return render(request, 'contacts.html')


