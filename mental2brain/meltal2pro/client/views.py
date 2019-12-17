from django.shortcuts import render



def index(request):
    
    return render(request,'client/index.html')

def home(request):
    
    return render(request,'client/profile/profile.html')