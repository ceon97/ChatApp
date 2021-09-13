from django.shortcuts import render, redirect
from mychat.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import Message





def home(request):
	return render(request, 'mychat/home.html')


def register(request):
        if request.method=="POST":
            form = RegisterForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect("/")   
        else:
            form = RegisterForm()
    
        return render(request, "mychat/register.html",{'form':form})

def login(request):    
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username, password=password)
            if user is not None:
                return redirect('/chat')
            else:
            	
            	form=AuthenticationForm()

            	  
        else:
        	form=AuthenticationForm()    
        return render(request, "mychat/login.html",{'form':form})

def index(request):
    return render(request, 'mychat/index.html',{})

def room(request, room_name):
    username=request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request,'mychat/room.html',{'room_name':room_name,'username':username,'messages': messages})   
    