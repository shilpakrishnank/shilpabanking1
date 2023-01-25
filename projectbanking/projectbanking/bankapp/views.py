from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def demo(request ):
    return render(request, "index1.html")
def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        userauth=auth.authenticate(username=username,password=password)
        if userauth is not None:
           auth.login(request,userauth)
           return redirect('new')
        else:
           messages.info(request,"invalid")
           return redirect('login')


    return render(request,"login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        # user=User.objects.create_user(username=username,password=password)
        userauth = auth.authenticate(username=username, password=password)
        if userauth is not None:
            auth.login(request, userauth)
            return redirect('login')
        userauth.save();
        return redirect('login')

    return render(request,'register.html')

def new(request):
        # return redirect('base')
        return render(request, 'new.html')


def form(request):
    if request.method == 'POST':
        return redirect('submit')
    return render(request, "form.html")


def submit(request):
    # return redirect('register')
    return render(request, 'submit.html')