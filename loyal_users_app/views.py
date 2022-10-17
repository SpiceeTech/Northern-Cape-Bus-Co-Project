from django.shortcuts import render
from .models import Buses

# Create your views here.
def loyal_users(request):
    buses = Buses.objects.all()
    context={
        'buses': buses
    }
    return render(request,'loyal_users.html', context)