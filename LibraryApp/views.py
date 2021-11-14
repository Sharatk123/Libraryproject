from django.shortcuts import render,redirect
from django.conf import settings
from .forms import AddBookForm,SignUpForm,SignInForm
from .models import AddBook,SignUp,SignIn
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate

# Create your views here.

def home(request):
    return render(request,'Home.html')

def Add_Book(request):
    if request.method=="POST":
        bl=AddBookForm(request.POST,request.FILES)
        if bl.is_valid:
            bl.save()
            return redirect('View_Order')
    else:
        bl=AddBookForm()
    return render(request,'Add_Book.html',{'blog':bl})

def View_Order(request):
    st=AddBook.objects.all()
    return render(request,'View_Order.html',{'st':st})

def delete_Order(request,pk):
    dl=AddBook.objects.get(pk=pk)
    dl.delete()
    return redirect('View_Order')

def contact(request):
    return render(request,'contact.html')

def update_book(request,pk):
    prod=AddBook.objects.get(pk=pk)
    form=AddBookForm(instance=prod)
    if request.method=="POST":
        form=AddBookForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect("View_Order")

    return render(request,'Add_Book.html',{'blog':form})

def about(request):
    return render(request,'about.html')

def register(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=name
        myuser.save()
        print('saved')
        return redirect('login')
    else:
        form=SignUpForm()
    return render(request,'register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        si=SignInForm(request.POST)
        if si.is_valid():
            username=si.cleaned_data['username']
            password=si.cleaned_data['password']
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            auth_login(request,myuser)
            return redirect('View_Order')
        else:
            return redirect('login')
    else:
        si=SignInForm()
    return render(request,'login.html',{'si':si})

def logout(request):
    auth_logout(request)
    return redirect('/')






