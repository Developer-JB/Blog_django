from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category, Blog
from . forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    context = {
        'featured_posts':featured_posts,
        'posts':posts
    }
    return render(request,'home-blogs.html',context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    context = {
        'form':form
    }

    return render(request,'register.html',context)

def Login(request):

    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)

            return redirect('/')

    form = AuthenticationForm()
    
    context ={

        'form':form

    }

    return render(request,'login.html',context)

def Logout(request):
    logout(request)
    return redirect('/')