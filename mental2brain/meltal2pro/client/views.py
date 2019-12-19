from django.shortcuts import render
from django.core import serializers
from .models import Coach



        
def login(request):
    return render(request, 'client/login.html')

def index(request):
    
    return render(request,'client/index.html')

def home(request):
    
    return render(request,'client/profile/profile.html')


def coachSearch(request):

    coachs = Coach.objects.all()
    data = serializers.serialize("json", Coach.objects.all())

    return render(request,'client/search-coach.html', {'data': data, 'coachs': coachs})

def chat(request):
    return render(request, 'client/chat.html',{})

def test(request):
    coachs = Coach.objects.all()
    data = serializers.serialize("json", Coach.objects.all())

    return render(request, 'client/blank.html',{'data': data, 'coachs': coachs})

def profile(request):
    return render(request, 'client/profile/profile.html',{})
