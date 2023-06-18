from django.shortcuts import render, HttpResponse,redirect
from django.template import loader
from django.contrib import messages
from home.models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def home(request):

    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 5 or len(content) < 4:
            messages.error(request, "please fill out the form correctly")
        else:
            print(name, email, phone, content)
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, 'Welcome to contact')

    return render(request, 'home/contact.html')


def about(request):
    messages.success(request, 'welcome to about')
    return render(request, 'home/about.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if len(username) < 10:
            messages.error(request,"your user name must be under 10 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"user name should only contain letters and numbers")
            return redirect('home')
        if(pass1 != pass2):
            messages.error(request,"passwords donot match")
            return redirect('home')

        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"your info has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404-Not found")

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect("home")

def handleLogin(request):
    if request.method == "POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['pass']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            # print(loginusername,loginpassword)
            return redirect("home")
        else:
            messages.error(request,"invalid credentials ! please try again")
            return redirect("home")
        return HttpResponse("404-Not found")
    


    
